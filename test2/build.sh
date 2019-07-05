#!/bin/bash
export COMMIT_SHA=$(git rev-parse HEAD)

docker build --build-arg APP_VERSION=$(cat VERSION.txt) \
    --build-arg COMMIT_SHA=$COMMIT_SHA -t anz_test2:$COMMIT_SHA .

