#!/bin/bash
sudo apt-get -o Dpkg::Options::="--force-confnew" install -y docker-engine=${DOCKER_VERSION}