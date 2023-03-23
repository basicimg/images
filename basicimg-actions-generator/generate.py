#!/opt/venv/bin/python3

import json
import os
import sys
import yaml

import jdk

GENERATED_HEADER = "# This was generated by basicimg-actions-generator. Run regenerate.sh/ps1 to regenerate.\n"

def panic(msg):
    print(msg)
    sys.exit(1)

def process_file(path, images = []):
    with open(path, "r") as stream:
        data = yaml.safe_load(stream)
    if "images" in data:
        images.extend(data["images"])
    if "include" in data:
        for file in data["include"]:
            process_file(file, images)
    return images

def generate_dockerfile(image):
    if "generate" in image and image["generate"]:
        path = image["path"]
        print(f"generating Dockerfile for {path}")
        dockerfilePath = f"./{path}/Dockerfile"
        base = image["base"]
        install = None
        if "install" in image:
            install = " ".join(image["install"])
        expose = None
        if "expose" in image:
            expose = image["expose"]
        healthcheck = None
        healthcheckInterval = None
        healthcheckTimeout = None
        healthcheckStartPeriod = None
        healthcheckRetries = None
        healthcheckCmd = None
        if "healthcheck" in image:
            healthcheck = image["healthcheck"]
            if "interval" in healthcheck:
                healthcheckInterval = healthcheck["interval"]
            if "timeout" in healthcheck:
                healthcheckTimeout = healthcheck["timeout"]
            if "startPeriod" in healthcheck:
                healthcheckStartPeriod = healthcheck["startPeriod"]
            if "retries" in healthcheck:
                healthcheckRetries = healthcheck["retries"]
            if "cmd" in healthcheck:
                healthcheckCmd = healthcheck["cmd"]
        cmd = None
        if "cmd" in image:
            cmd = image["cmd"]
        app = image["app"]
        copy = []
        if "copy" in image:
            copy = image["copy"]
        image["dependencies"] = [base]
        os.makedirs(path, exist_ok=True)
        with open(dockerfilePath, "w") as file:
            file.write("# syntax=docker/dockerfile:1\n")
            file.write(GENERATED_HEADER)
            file.write(f"FROM {base}\n")
            if install != None:
                file.write(f"RUN basicimg-install {install}\n")
            for toCopy in copy:
                copyFrom = toCopy["from"]
                copyTo = toCopy["to"]
                file.write(f"COPY {copyFrom} {copyTo}\n")
            file.write(f"RUN basicimg-setapp \"{app}\"\n")
            if expose != None:
                if isinstance(expose, list):
                    for port in expose:
                        file.write(f"EXPOSE {port}\n")
                else:
                    file.write(f"EXPOSE {expose}\n")
            if healthcheck != None:
                file.write("HEALTHCHECK")
                if healthcheckInterval != None:
                    file.write(f" --interval={healthcheckInterval}")
                if healthcheckTimeout != None:
                    file.write(f" --timeout={healthcheckTimeout}")
                if healthcheckStartPeriod != None:
                    file.write(f" --start-period={healthcheckStartPeriod}")
                if healthcheckRetries != None:
                    file.write(f" --retries={healthcheckRetries}")
                if healthcheckCmd != None:
                    healthcheckCmdJson = json.dumps(healthcheckCmd)
                    file.write(f" CMD {healthcheckCmdJson}")
                file.write("\n")
            if cmd != None:
                cmdJson = json.dumps(cmd)
                file.write(f"CMD {cmdJson}\n")

def image_slug(image):
    return image["path"].replace("/", "_").replace(".", "_")

def image_to_job(image):
    path = image["path"]
    print(f"generating job for path {path}")
    if not os.path.isfile(f"./{path}/Dockerfile"):
        panic(f"missing dockerfile for path {path}")
    tags = image["tags"]
    labels = [
        f"com.github.basicimg.path={path}"
    ]
    if "description" in image:
        description = image["description"]
        labels.append(f"org.opencontainers.image.description={description}")
    steps = [
        {
            "name": "Checkout repository",
            "uses": "actions/checkout@v3"
        },
        {
            "name": "Setup Docker Buildx",
            "uses": "docker/setup-buildx-action@v2"
        },
        {
            "name": "Login to container registry",
            "uses": "docker/login-action@v2",
            "with": {
                "registry": "ghcr.io",
                "username": "${{ github.actor }}",
                "password": "${{ secrets.GITHUB_TOKEN }}"
            }
        },
        {
            "name": "Generate metadata",
            "id": "meta",
            "uses": "docker/metadata-action@v4",
            "with": {
                "images": "dummy",
                "labels": "\n".join(labels)
            }
        },
        {
            "name": "Build and push image",
            "uses": "docker/build-push-action@v4",
            "with": {
                "push": True,
                "cache-from": "type=gha",
                "cache-to": "type=gha,mode=max",
                "tags": ",".join(tags),
                "labels": "${{ steps.meta.outputs.labels }}",
                "file": f"./{path}/Dockerfile"
            }
        },
        {
            "name": "Run `basicimg-hello`",
            "run": f"docker run --rm {tags[0]} basicimg-hello"
        }
    ]
    if "test" in image:
        test = image["test"]
        steps.append({
            "name": "Run test",
            "run": f"docker run --rm {tags[0]} /bin/sh -euxc '{test}'"
        })
    integration = None
    if "integration" in image:
        integration = image["integration"]
        integrationImage = tags[0]
        if "image" in integration:
            integrationImage = integration["image"]
        integrationTest = integration["test"]
        dockerArgs = ""
        if "dockerArgs" in integration:
            dockerArgs = integration["dockerArgs"]
        steps.append({
            "name": "Run integration test",
            "run": f"docker run -d {dockerArgs} --name main {tags[0]} && docker run --network host --rm {integrationImage} /bin/sh -euxc '{integrationTest}' && docker rm -f main"
        })
    job = {
        "name": path,
        "runs-on": "ubuntu-22.04",
        "permissions": {
            "contents": "read",
            "packages": "write"
        },
        "steps": steps
    }
    needs = []
    if "dependencies" in image:
        needs.extend([image_slug(imagesByTag[dep]) for dep in image["dependencies"]])
    if integration != None and "image" in integration:
        needs.append(integration["image"])
    if len(needs) > 0:
        job["needs"] = needs
    return job

def generate_workflow(jobs):
    return {
        "name": "build",
        "concurrency": "build",
        "on": {
            "push": {
                "branches": [
                    "main"
                ]
            },
            "schedule": [
                {
                    "cron": "5 4 * * 1"
                }
            ]
        },
        "jobs": jobs
    }

images = process_file("images.yaml")
images.extend(jdk.generate_jdk_images())
for image in images:
    generate_dockerfile(image)
imagesByTag = {}
for image in images:
    for tag in image["tags"]:
        if tag in imagesByTag:
            panic(f"duplicate tag: {tag}")
        imagesByTag[tag] = image
jobs = { image_slug(image): image_to_job(image) for image in images }
workflow = generate_workflow(jobs)

with open(".github/workflows/ci.yaml", "w") as stream:
    stream.write(GENERATED_HEADER)
    yaml.dump(workflow, stream)

print(f"Processed {len(images)} images.")
