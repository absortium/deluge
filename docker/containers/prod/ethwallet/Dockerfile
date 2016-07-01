FROM absortium/base-ethwallet

# Install gunicorn
RUN pip3 install gunicorn

# Setup core in develop mode
COPY "$CORE_PATH" "$CORE_PATH"
RUN pip3 install "$CORE_PATH"

# Copy whole project, because in 'prod' we do not mount directories.
COPY "$APP_PATH" "$APP_PATH"
RUN chown -R "$UNAME:$UNAME" "$APP_PATH"

# Log in as user
USER "$UNAME"

WORKDIR "$DOCKER_PROJECT_PATH/$APP_PATH"
