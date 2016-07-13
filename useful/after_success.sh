#!/bin/bash

set -e
shopt -s expand_aliases

declare GREEN='\033[0;32m'
declare NC='\033[0m'
print () {
    echo -e "${GREEN}$1${NC}"
}

declare DOCKER_USER="$1"
declare DOCKER_PASS="$2"
declare SERVICE="$3"
declare BRANCH="$4"

export DELUGE_PATH="$PWD"

echo "SERVICE=$SERVICE"
echo "BRANCH=$BRANCH"
echo "DELUGE_PATH=$DELUGE_PATH"

print "Step #0: Install aliases."
for f in $DELUGE_PATH/useful/aliases/*; do
    echo "Install aliases from: $f"
    source "$f"
done

if [[ -n "$BRANCH" && -n "$DOCKER_USER" && -n "$DOCKER_USER" ]]; then
    print "Step #1 Login to the DockerHub"
    docker login -u "$DOCKER_USER" -p "$DOCKER_PASS"

    if [ "$BRANCH" == "master" ]; then
        declare IMAGE="$SERVICE"

        print "Step #2: Switch to the 'realnet' mode."
        dcinit realnet

        print "Step #3: Build $IMAGE image."
        dc build frontend

    elif [ "$BRANCH" == "development" ]; then
        declare IMAGE="base-$SERVICE"

        print "Step #2: Switch to the 'unit' mode."
        dcinit unit

        print "Step #3: Image $IMAGE should be already built."
    fi

    if [ -n "$IMAGE" ]; then
        print "Step #4: Push '$IMAGE' image on docker hub"
        docker push "absortium/$IMAGE:latest"
    fi
fi
