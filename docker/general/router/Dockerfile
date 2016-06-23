# Pull base image.
FROM python:3.5

MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH  "services/router"
ENV DOCKER_PROJECT_PATH  "/opt/deluge"

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

RUN apt-get update && pip3 install --upgrade pip

# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH"

RUN mkdir ".crossbar"

# Setup app
COPY "$APP_PATH/.crossbar/config.json" "$APP_PATH/.crossbar/config.json"

# Setup app
COPY "$APP_PATH/requirements.txt" "$APP_PATH/requirements.txt"
RUN pip3 --no-cache-dir install -r "$APP_PATH/requirements.txt"

CMD crossbar start --cbdir="$APP_PATH/.crossbar/"

