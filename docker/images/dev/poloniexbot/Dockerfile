FROM absortium/base-poloniexbot

ENV LIBS_PATH "libs"

COPY "$LIBS_PATH/core" "$LIBS_PATH/core"
COPY "$LIBS_PATH/absortium-api" "$LIBS_PATH/absortium-api"
COPY "$LIBS_PATH/poloniex-api" "$LIBS_PATH/poloniex-api"

RUN chown -R "$UNAME:$UNAME" "$LIBS_PATH"

RUN pip3 install -e "$LIBS_PATH/core"
RUN pip3 install -e "$LIBS_PATH/absortium-api"
RUN pip3 install -e "$LIBS_PATH/poloniex-api"

# Log in as ethereum user
USER "$UNAME"

WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH"
