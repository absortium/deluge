# Pull base image.
FROM python:3.5

MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH  "services/backend/src"
ENV CORE_PATH "services/backend/libs/core"

ENV DOCKER_PROJECT_PATH  "/opt/deluge"

RUN apt-get update
RUN pip3 install --upgrade pip

# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH"

# Setup core in develop mode
COPY "$CORE_PATH" "$CORE_PATH"
RUN pip3 install -e "$CORE_PATH"

# Setup app
COPY "$APP_PATH/requirements.txt" "$APP_PATH/requirements.txt"
RUN pip3 --no-cache-dir install -r "$APP_PATH/requirements.txt"

WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH/"

ENTRYPOINT ["python3", "-u", "manage.py"]
CMD ["runserver" , "0.0.0.0:3000"]

