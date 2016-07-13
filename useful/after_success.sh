#!/bin/bash

set -e
shopt -s expand_aliases

declare GREEN='\033[0;32m'
declare NC='\033[0m'
print () {
    echo -e "${GREEN}$1${NC}"
}

declare DOCKER_EMAIL="$1"
declare DOCKER_USER="$2"
declare DOCKER_PASS="$3"
declare SERVICE="$4"
declare BRANCH="$5"

echo "SERVICE=$SERVICE"
echo "BRANCH=$BRANCH"

print "Step #0: Install aliases."
for f in "$DELUGE_PATH/useful/aliases/*"; do
    echo "Install aliases from: $f"
    source "$f"
done

if [ -n "$BRANCH" ]; then
    print "Step #1 Login to the DockerHub"
    docker login -e "$DOCKER_EMAIL" -u "$DOCKER_USER" -p "$DOCKER_PASS"

    if [ "$BRANCH" == "master" ]; then
        declare IMAGE="absortium/$SERVICE"

        print "Step #2: Switch to the 'realnet' mode."
        dcinit realnet

        print "Step #3: Build $IMAGE image."
        dc build frontend

    elif [ "$BRANCH" == "development" ]; then
        declare IMAGE="absortium/base-$SERVICE"

        print "Step #2: We already in 'unit' mode."
        print "Step #3: Image $IMAGE already built."
    fi

    print "Step #2 Push image - $IMAGE on docker hub"
    docker push "$IMAGE"
fi
