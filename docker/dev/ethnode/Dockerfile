# Pull base image.
FROM ethereum/client-go

MAINTAINER Andrey Samokhvalov (andrew.shvv@gmail.com)

ENV APP_PATH  "services/ethnode"
ENV DOCKER_PROJECT_PATH  "/opt/deluge"

RUN apt-get update
#RUN pip3 install --upgrade pip
RUN apt-get install -y socat

# Add non-root user in order to run celery
RUN groupadd ethereum && useradd -g ethereum ethereum

# Create and cd to the workdir
WORKDIR "$DOCKER_PROJECT_PATH"

# Create ethereum data dir
RUN mkdir -p "$APP_PATH"

# Change previlage
RUN chown ethereum "$APP_PATH"

# Create an ethereum data mount point
VOLUME ["$DOCKER_PROJECT_PATH/$APP_PATH"]

# Log in as ethereum user
USER ethereum

WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH"

# 'ethereum/client-go' already has 'geth' entrypoint
CMD ["--datadir" , ".",  "--rpcapi", "personal,eth,web3,net",  "--rpc", "--rpcaddr" ,"0.0.0.0"]
