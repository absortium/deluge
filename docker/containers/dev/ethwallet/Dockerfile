FROM absortium/base-ethwallet

COPY "$CORE_PATH" "$CORE_PATH"

# Setup core in develop mode
RUN pip3 install -e "$CORE_PATH"

# Log in as ethereum user
USER "$UNAME"

WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH"
