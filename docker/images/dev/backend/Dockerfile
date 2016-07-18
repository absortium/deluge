FROM absortium/base-backend

ENV LIBS_PATH "libs/"

COPY "$LIBS_PATH/core" "$LIBS_PATH/core"
COPY "$LIBS_PATH/ethwallet" "$LIBS_PATH/ethwallet"
COPY "$LIBS_PATH/poloniex" "$LIBS_PATH/poloniex"

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