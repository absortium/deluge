#!/bin/bash

set -e
shopt -s expand_aliases

declare GREEN='\033[0;32m'
declare NC='\033[0m'
print () {
    echo -e "${GREEN}$1${NC}"
}

declare SERVICE="$1"
echo "SERVICE=$SERVICE"

declare BRANCH="$2"
echo "BRANCH=$BRANCH"

declare TRAVIS="$3"
if [ -z $TRAVIS ]; then
    TRAVIS="false"
fi
echo "TRAVIS=$TRAVIS"

export DELUGE_PATH="$PWD"
echo "DELUGE_PATH=$DELUGE_PATH"

print "Step #0: Install aliases."
for f in $DELUGE_PATH/useful/aliases/*; do
    echo  "Install aliases from: $f"
    source "$f"
done

print  "Step #1: Turn on 'unit' mode."
dcinit unit

if [ -n $BRANCH ]; then
    pushd services/$SERVICE
    git checkout $BRANCH
    git pull
    popd
fi

echo """$(tree "$DELUGE_PATH/services/$SERVICE")"""


case "$SERVICE" in
    'frontend' )
        if [ "$TRAVIS" == "true" ]; then
            print "Step #2: Build 'base-frontend' service."
            dc build base-frontend
        else
            print "Step #2: Skip build 'base-frontend' service, it will be downloaded from docker hub on Step #3."
        fi

        print "Step #3: Install frontend and run tests."
        dc run frontend run test

        ;;

    'backend' )
        print "Step #2: Install and run 'postgres' service."
        dc up -d postgres

        if [ "$TRAVIS" == "true" ]; then
            print "Step #3: Build 'base-backend' service."
            dc build base-backend
        else
            print "Step #3: Skip build 'base-backend' service, it will be downloaded from docker hub on Step #4."
        fi


        print "Step #4: Build 'backend' service."
        dc build backend

        print "Step #5: Migrate database."
        dc run m-backend migrate

        print "Step #6: Run tests."
        dc run m-backend test --verbosity 2 absortium.tests.unit

        ;;

    'ethwallet' )
        print "Step #2: Install and run 'postgres' service."
        dc up -d postgres

        if [ "$TRAVIS" == "true" ]; then
            print "Step #3: Build 'base-backend' service."
            dc build base-ethwallet
        else
            print "Step #3: Skip build 'base-backend' service, it will be downloaded from docker hub on Step #4."
        fi

        print "Step #4: Build 'ethwallet' service."
        dc build ethwallet

        print "Step #5: Create 'ethwallet' database."
        dex postgres psql -c "CREATE DATABASE ethwallet" -U postgres

        print "Step #6: Migrate database."
        dc run m-ethwallet migrate

        print "Step #7: Run tests."
        dc run m-ethwallet test --verbosity 2 ethwallet.tests.unit

        ;;

    *)
        print "Can't find any services similar to '$1'"
        break
esac

