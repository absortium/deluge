FROM absortium/base-frontend

COPY "$APP_PATH" "."

RUN npm run build && npm prune --production
RUN apt-get purge && apt-get clean