FROM absortium/base-backend

ENV LIBS_PATH "libs"

COPY "$LIBS_PATH/core" "$LIBS_PATH/core"
COPY "$LIBS_PATH/ethwallet-api" "$LIBS_PATH/ethwallet-api"
COPY "$LIBS_PATH/poloniex-api" "$LIBS_PATH/poloniex-api"

RUN chown -R "$UNAME:$UNAME" "$LIBS_PATH"

# Setup core in develop mode
RUN pip3 install -e "$LIBS_PATH/core"

# Setup ethwallet in develop mode
RUN pip3 install -e "$LIBS_PATH/ethwallet-api"

# Setup poloniex in develop mode
RUN pip3 install -e "$LIBS_PATH/poloniex-api"

# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH/"

USER "$UNAME"