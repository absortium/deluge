#!/bin/bash

set -e
shopt -s expand_aliases

declare SERVICE="$1"

declare GREEN='\033[0;32m'
declare NC='\033[0m'
print () {
    echo -e "${GREEN}$1${NC}"
}

export DELUGE_PATH="$PWD"

# For simplicity I prefer use aliases which I developed for this project, on first sign it might look overwhelming, but
# I think it may significantly help for developing.
print "Step #0: Install aliases."
for f in $DELUGE_PATH/useful/aliases/*; do
    echo  "Install aliases from: $f"
    source "$f"
done

print  "Step #1: Turn on 'unit' mode."
dcinit unit

case "$SERVICE" in
    'frontend' )
        print "Step #2: Build 'base-frontend' service."
        dc build base-frontend

        print "Step #3: Install frontend and run tests."
        dc run frontend run test

        ;;

    'backend' )
        print "Step #2: Install and run 'postgres' service."
        dc up -d postgres

        print "Step #3: Build 'base-backend' service."
        dc build base-backend

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

        print "Step #3: Build 'base-backend' service."
        dc build base-ethwallet

        print "Step #4: Build 'backend' service."
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

