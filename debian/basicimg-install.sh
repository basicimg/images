#!/bin/sh

set -eux

apt-get update
apt-get install --no-install-recommends -y "$@"
apt-get clean
rm -rf /var/lib/apt/lists/*
