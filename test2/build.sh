#!/bin/bash
export COMMIT_SHA=$(git rev-parse HEAD)

if [ -n $PROJECT_ID ]; then
  TAG="gcr.io/${PROJECT_ID}/anz_test2:${COMMIT_SHA}"
else
  TAG="anz_test2:${COMMIT_SHA}"
fi

docker build --build-arg APP_VERSION=$(cat VERSION.txt) \
    --build-arg COMMIT_SHA=$COMMIT_SHA -t $TAG .

