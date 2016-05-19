# Pull base image.
FROM python:3.5

MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH  "services/backend/src"
ENV LIBS_PATH "services/backend/libs/"
ENV DOCKER_PROJECT_PATH  "/opt/deluge"

RUN apt-get update
RUN pip3 install --upgrade pip

# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH"

COPY "$LIBS_PATH" "$LIBS_PATH"

# Setup core in develop mode
RUN pip3 install -e "$LIBS_PATH/core"

# Setup ethwallet in develop mode
RUN pip3 install -e "$LIBS_PATH/ethwallet"

# Setup app
COPY "$APP_PATH/requirements.txt" "$APP_PATH/requirements.txt"
RUN pip3 --no-cache-dir install -r "$APP_PATH/requirements.txt"

# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH/"

# Add non-root user in order to run celery
RUN groupadd user && useradd -g user user
USER user