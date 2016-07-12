#!/bin/bash

set -ev

if [ $TRAVIS == "true" ] ; then
    git clone --recursive https://github.com/absortium/deluge.git
    cd deluge
fi

export DELUGE_PATH="$PWD"
export DEFAULT_MODE="frontend"

# For simplicity I prefer use aliases which I developed for this project, on first sign it might look overwhelming, but
# I think it may significantly help for developing.
for f in $DELUGE_PATH/useful/aliases/*; do
  source "$f"
done

gods frontend; git checkout development
gods backend; git checkout development
gods ethwallet; git checkout development

# Turn on 'unit' mode (is using for testing)
echo "dcinit unit"

# Install and run `postgres` service.
echo "dc up -d postgres"

# Build `backend` service.
echo "dc build backend"

# Migrate database.
echo "dc run m-backend migrate"

# Install frontend and run tests
echo "dc run frontend run test"

# Turn on 'frontend' mode
echo "dcinit frontend"

# Run frontend
echo "dc up frontend"
