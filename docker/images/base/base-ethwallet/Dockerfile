# Pull base image.
FROM python:3.5

MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH "services/ethwallet"
ENV DOCKER_PROJECT_PATH  "/opt/deluge"
ENV UNAME "docker"

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

# Add non-root user in order to run celery
RUN groupadd "$UNAME" && useradd -g "$UNAME" "$UNAME"

RUN apt-get update && pip3 install --upgrade pip

WORKDIR "$DOCKER_PROJECT_PATH"

# Copy only requirements.txt in order to install dependencies
COPY "$APP_PATH/requirements.txt" "$APP_PATH/requirements.txt"
RUN pip3 --no-cache-dir install -r "$APP_PATH/requirements.txt"