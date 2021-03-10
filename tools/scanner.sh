#!/bin/sh


SONAR_LOGIN=$1

docker run \
    --rm \
    --network host \
    -e SONAR_HOST_URL="http://sq.refactored.ai" \
    -e SONAR_LOGIN="$SONAR_LOGIN" \
    -v $(pwd):/usr/src \
    sonarsource/sonar-scanner-cli

