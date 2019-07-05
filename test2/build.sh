#!/bin/bash

docker build --build-arg APP_VERSION=$(cat VERSION.txt) \
    --build-arg COMMIT_SHA=$(git rev-parse HEAD) -t anz_test2 .
