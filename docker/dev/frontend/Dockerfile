FROM node:latest
MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH  "services/frontend"
ENV DOCKER_PROJECT_PATH  "/opt/deluge"

# Install dependencies
WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH"

COPY "$APP_PATH" "."

RUN npm cache clean
RUN npm install grunt -g
RUN npm install grunt-cli -g
RUN npm install bower  -g
RUN npm install
RUN bower --allow-root install

## Start the app
CMD grunt serve