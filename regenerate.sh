#!/bin/bash

set -euxo pipefail

docker build -t ghcr.io/basicimg/basicimg-actions-generator:dev -f basicimg-actions-generator/Dockerfile --progress=plain .
docker run --rm --volume .:/repo ghcr.io/basicimg/basicimg-actions-generator:dev