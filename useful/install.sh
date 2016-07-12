#!/bin/bash

set -ev

declare TRAVIS_REPO_SLUG="$1"
declare TRAVIS_BRANCH="$2"
declare REPOSITORY=$(echo "$TRAVIS_REPO_SLUG" | python -c "import sys; print(sys.stdin.read().split()[1])")

echo "$TRAVIS_REPO_SLUG"
echo "$TRAVIS_BRANCH"
echo "$REPOSITORY"

git clone --recursive https://github.com/absortium/deluge.git
cd deluge

export DELUGE_PATH="$PWD"

# For simplicity I prefer use aliases which I developed for this project, on first sign it might look overwhelming, but
# I think it may significantly help for developing.
for f in $DELUGE_PATH/useful/aliases/*; do
  source "$f"
done

gods "$REPOSITORY"; git checkout "$TRAVIS_BRANCH"

# Turn on 'unit' mode (is using for testing)
echo "dcinit unit"

# Install and run `postgres` service.
echo "dc up -d postgres"

# Build `base-backend` service.
echo "dc build base-backend"

# Build `backend` service.
echo "dc build backend"

# Migrate database.
echo "dc run m-backend migrate"

# Install frontend and run tests
echo "dc run frontend run test"
