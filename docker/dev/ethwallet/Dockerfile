# Pull base image.
FROM python:3.5

MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH "services/ethwallet"
ENV CORE_PATH "services/backend/libs/core"
ENV ETHEREUM_NODE_PATH "services/ethnode"

ENV DOCKER_PROJECT_PATH  "/opt/deluge"

RUN apt-get update
RUN pip3 install --upgrade pip


# Add non-root user in order to run celery
RUN groupadd ethereum && useradd -g ethereum ethereum

WORKDIR "$DOCKER_PROJECT_PATH"

# Create ethereum data dir
RUN mkdir -p "$ETHEREUM_NODE_PATH"

# Change previlage
RUN chown ethereum "$ETHEREUM_NODE_PATH"

# Create an ethereum data mount point
VOLUME ["$ETHEREUM_NODE_PATH"]

# Setup core in develop mode
COPY "$CORE_PATH" "$CORE_PATH"
RUN pip3 install -e "$CORE_PATH"

# Setup app
COPY "$APP_PATH/requirements.txt" "$APP_PATH/requirements.txt"
RUN pip3 --no-cache-dir install -r "$APP_PATH/requirements.txt"

# Log in as ethereum user
#USER ethereum

WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH"
