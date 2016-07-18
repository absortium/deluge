FROM absortium/base-ethwallet

ENV LIBS_PATH "libs"

COPY "$LIBS_PATH/core" "$LIBS_PATH/core"

# Setup core in develop mode
RUN pip3 install -e "$LIBS_PATH/core"

# Log in as ethereum user
USER "$UNAME"

WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH"
