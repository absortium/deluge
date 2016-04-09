FROM node:latest
MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH  "frontend"
ENV DOCKER_PROJECT_PATH  "/opt/absortium"

# Install dependencies
WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH"

COPY "$APP_PATH" "."

RUN npm install grunt grunt-cli bower -g
RUN npm install
RUN bower --allow-root install

## Start the app
CMD grunt serve