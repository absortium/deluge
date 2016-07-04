FROM absortium/base-backend

COPY "$LIBS_PATH" "$LIBS_PATH"
RUN chown -R "$UNAME:$UNAME" "$LIBS_PATH"

# Setup core in develop mode
RUN pip3 install -e "$LIBS_PATH/core"

# Setup ethwallet in develop mode
RUN pip3 install -e "$LIBS_PATH/ethwallet"

# Setup poloniex in develop mode
RUN pip3 install -e "$LIBS_PATH/poloniex"

# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH/"

USER "$UNAME"