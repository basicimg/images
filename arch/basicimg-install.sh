#!/bin/sh

set -eux

pacman -Sy --noconfirm "$@"
rm -rf /var/cache/pacman/*
