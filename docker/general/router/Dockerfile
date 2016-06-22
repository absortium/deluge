# Pull base image.
FROM python:3.5

MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH  "services/router"
ENV DOCKER_PROJECT_PATH  "/opt/deluge"

RUN apt-get update
RUN pip3 install --upgrade pip

# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH"

# Setup app
COPY "$APP_PATH/requirements.txt" "$APP_PATH/requirements.txt"
RUN pip3 --no-cache-dir install -r "$APP_PATH/requirements.txt"

CMD crossbar start --cbdir="$APP_PATH/.crossbar/"

