#!/bin/sh

set -eux

xbps-install --reproducible --yes -S "$@"
rm -rf /var/cache/xbps/*