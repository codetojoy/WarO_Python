#!/bin/bash

docker run \
    --rm --name waro-python \
    -i --log-driver=none -a stdin -a stdout -a stderr \
    -v $(pwd):/tmp \
    python:latest \
    python3 /tmp/waro/main.py

