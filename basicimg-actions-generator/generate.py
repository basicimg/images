#!/usr/bin/python3

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
    labels = [
        "org.opencontainers.image.source=https://github.com/basicimg/images"
    ]
    if "description" in image:
        description = image["description"]
        labels.append(f"org.opencontainers.image.description={description}")
    job = {
        "name": tags[0],
        "runs-on": "ubuntu-22.04",
        "permissions": {
            "contents": "read",
            "packages": "write"
        },
        "steps": [
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
                "name": "Build and push image",
                "uses": "docker/build-push-action@v4",
                "with": {
                    "push": True,
                    "cache-from": "type=gha",
                    "cache-to": "type=gha,mode=max",
                    "tags": ",".join(tags),
                    "labels": ",".join(labels),
                    "file": f"./{path}/Dockerfile"
                }
            }
        ]
    }
    if "dependencies" in image:
        job["needs"] = [image_slug(imagesByTag[dep]) for dep in image["dependencies"]]
    return job

def generate_workflow(jobs):
    return {
        "name": "ci",
        "on": {
            "push": {
                "branches": [
                    "main"
                ]
            }
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
    yaml.dump(workflow, stream)

print(f"Processed {len(images)} images.")