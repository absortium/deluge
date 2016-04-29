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


# Watch for django test database in realtime
func_watchpsql() {
    watch -n 0.2 "psql -h absortium.com -p 5432 -U postgres -d test_postgres -c '$1'"
}
alias watchpsql=func_watchpsql


# stream copying folder/file from the docker machine
# Example: dmstreamcopy /mnt/sda1/var/lib/docker/volumes/dev_ethereumdata/_data ~/Downloads/blockchaindata/
func_streamcopy() {
    mkdir -p "$2"
    docker-machine ssh default "sudo -u root tar czpf - -C $1 . " | pipemeter |tar xzpf - -C $2
}
alias dmstreamcopy=func_streamcopy
