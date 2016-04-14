# Pull base image.
FROM celery

MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH  "services/backend/src"
ENV DOCKER_PROJECT_PATH  "/opt/deluge"

## Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH"

## Setup core in develop mode
#COPY "$CORE_PATH" "$CORE_PATH"
#RUN pip3 install -e "$CORE_PATH"

ENTRYPOINT ["celery"]
CMD ["-A" , "absortium.celery.app", "worker", "--loglevel=info"]
