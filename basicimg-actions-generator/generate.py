#!/opt/venv/bin/python3

import sys
import yaml

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

def image_slug(image):
    return image["path"].replace("/", "_").replace(".", "_")

def image_to_job(image):
    path = image["path"]
    tags = image["tags"]
    labels = []
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
imagesByTag = {}
for image in images:
    for tag in image["tags"]:
        if tag in imagesByTag:
            panic(f"duplicate tag: {tag}")
        imagesByTag[tag] = image
jobs = { image_slug(image): image_to_job(image) for image in images }
workflow = generate_workflow(jobs)

with open(".github/workflows/ci.yaml", "w") as stream:
    stream.write("# This was generated by basicimg-actions-generator. Run regenerate.sh/ps1 to regenerate.\n")
    yaml.dump(workflow, stream)

print(f"Processed {len(images)} images.")
