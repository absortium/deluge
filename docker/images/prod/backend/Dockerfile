FROM absortium/base-backend

COPY "$LIBS_PATH" "$LIBS_PATH"
RUN chown -R "$UNAME:$UNAME" "$LIBS_PATH"

# Install gunicorn
RUN pip3 install gunicorn

# Setup core
RUN pip3 install "$LIBS_PATH/core"

# Setup ethwallet
RUN pip3 install "$LIBS_PATH/ethwallet"

# Copy whole project, because in 'prod' we do not mount directories.
COPY "$APP_PATH" "$APP_PATH"
RUN chown -R "$UNAME:$UNAME" "$APP_PATH"

# Define working directory.
WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH/"

USER "$UNAME"