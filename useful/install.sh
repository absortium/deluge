#!/bin/bash

set -ev

declare SERVICE="$1"
echo "$SERVICE"

export DELUGE_PATH="$PWD"

# For simplicity I prefer use aliases which I developed for this project, on first sign it might look overwhelming, but
# I think it may significantly help for developing.

echo "Step #0: Install aliases."
for f in $DELUGE_PATH/useful/aliases/*; do
  source "$f"
done

echo "Step #1: Turn on 'unit' mode (is using for testing)."
dcinit unit

echo "Step #2: Install and run 'postgres' service."
dc up -d postgres

echo "Step #3: Build 'base-backend' service."
dc build base-backend

echo "Step #4: Build 'backend' service."
dc build backend

echo "Step #5  Migrate database."
dc run m-backend migrate

echo "Step #6: Install frontend and run tests"
dc run frontend run test
