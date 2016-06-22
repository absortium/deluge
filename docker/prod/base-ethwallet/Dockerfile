# Pull base image.
FROM python:3.5

MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH "services/ethwallet"
ENV CORE_PATH "services/backend/libs/core"

ENV DOCKER_PROJECT_PATH  "/opt/deluge"

RUN apt-get update
RUN pip3 install --upgrade pip


# Add non-root user in order to run celery
RUN groupadd ethereum && useradd -g ethereum ethereum

WORKDIR "$DOCKER_PROJECT_PATH"

# Setup core
COPY "$CORE_PATH" "$CORE_PATH"
RUN pip3 install "$CORE_PATH"

# Setup app
COPY "$APP_PATH" "$APP_PATH"
RUN pip3 --no-cache-dir install -r "$APP_PATH/requirements.txt"

# Log in as ethereum user
USER ethereum

WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH"
