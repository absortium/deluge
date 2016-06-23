# Pull base image.
FROM python:3.5

MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH  "services/backend/src"
ENV LIBS_PATH "services/backend/libs/"
ENV DOCKER_PROJECT_PATH  "/opt/deluge"

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

RUN apt-get update && pip3 install --upgrade pip && pip3 install gunicorn


# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH"

COPY "$LIBS_PATH" "$LIBS_PATH"

# Setup core
RUN pip3 install "$LIBS_PATH/core"

# Setup ethwallet
RUN pip3 install "$LIBS_PATH/ethwallet"

# Setup app
COPY "$APP_PATH" "$APP_PATH"
RUN pip3 --no-cache-dir install -r "$APP_PATH/requirements.txt"

# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH/"

# Add non-root user in order to run celery
RUN groupadd user && useradd -g user user
USER user