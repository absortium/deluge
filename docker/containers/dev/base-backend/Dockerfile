# Pull base image.
FROM python:3.5

MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH  "services/backend/src"
ENV LIBS_PATH "services/backend/libs/"
ENV DOCKER_PROJECT_PATH  "/opt/deluge"
ENV NAME "docker"

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

# Add non-root user in order to run celery
RUN groupadd "$NAME" && useradd -g "$NAME" "$NAME"

RUN apt-get update && pip3 install --upgrade pip

# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH"

COPY "$LIBS_PATH" "$LIBS_PATH"
RUN chown -R "$NAME:$NAME" "$LIBS_PATH"

# Setup core in develop mode
RUN pip3 install -e "$LIBS_PATH/core"

# Setup ethwallet in develop mode
RUN pip3 install -e "$LIBS_PATH/ethwallet"

# Setup app
COPY "$APP_PATH/requirements.txt" "$APP_PATH/requirements.txt"
RUN pip3 --no-cache-dir install -r "$APP_PATH/requirements.txt"

# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH/"

USER "$NAME"