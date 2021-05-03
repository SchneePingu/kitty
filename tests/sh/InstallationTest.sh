#!/usr/bin/env bash

tar -xvf kitty.tar.gz
cd kitty-*
./configure --prefix="$HOME/.local"
make --dry-run
