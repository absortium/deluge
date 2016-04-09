# Pull base image.
FROM python:3.5

MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH  "src/info"
ENV POLONIEX_PATH "libs/poloniex"
ENV CORE_PATH "libs/core"

ENV DOCKER_PROJECT_PATH  "/opt/deluge"

RUN apt-get update && pip3 install --upgrade pip

# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH"


COPY "$POLONIEX_PATH" "$POLONIEX_PATH"
RUN pip3 install "$POLONIEX_PATH"

COPY "$CORE_PATH" "$CORE_PATH"
RUN pip3 install "$CORE_PATH"

COPY "$APP_PATH" "$APP_PATH"
RUN pip3 --no-cache-dir install -r "$APP_PATH/requirements.txt"

CMD python3 "$APP_PATH/client.py"

