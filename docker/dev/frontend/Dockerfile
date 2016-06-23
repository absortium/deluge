FROM node:latest
MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH  "services/frontend"
ENV DOCKER_PROJECT_PATH  "/opt/deluge"

# Install dependencies
WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH"

COPY "$APP_PATH" "."

RUN npm run preinstall && npm install && npm run postinstall

ENTRYPOINT ["npm"]
CMD ["-l"]