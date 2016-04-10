#!/usr/bin/env bash
# ------------------------------------
# Deluge alias and function
# ------------------------------------

export DELUGE_DIR="$PWD/PycharmProjects/deluge/"

# Go to the deluge directory
alias god="cd $DELUGE_DIR"

# Go to the deluge docker dev directory
alias godd="cd $DELUGE_DIR/docker/dev"

# Go to the deluge services directory
alias gods="cd $DELUGE_DIR/services"

# Init deluge project
ideluge() {
    source "$DELUGE_DIR/environments/secrets.sh"
}

# Delete crossbar process files if you forgot to shutdown router gracefully
cleancrossbar() {
    rm "$DELUGE_DIR/services/router/.crossbar/node.key"
    rm "$DELUGE_DIR/services/router/.crossbar/node.pid"
}
