#!/usr/bin/env bash
# ------------------------------------
# Deluge alias and function
# ------------------------------------

# Init deluge project
ideluge() {
    source "$DELUGE_PATH/.sensitive"
}

# Go to the deluge directory
func_god() {
    declare -a DIRS=("$DELUGE_PATH" $@)

    ## now loop through the above array
    CD_PATH=""
    for i in "${DIRS[@]}"
    do
        CD_PATH="$CD_PATH/$i"
        CD_PATH=$(echo "$CD_PATH" | sed "s#//*#/#g")
    done

    cd "$CD_PATH"
}
alias god=func_god

# Go to the deluge docker directory
func_godd() {
    ideluge
    func_god "/docker" $@
}
alias godd=func_godd

# Go to the deluge services directory
func_gods() {
    func_god "/services" "$@"
}
alias gods=func_gods

# Delete crossbar process files if you forgot to shutdown router gracefully
cleancrossbar() {
    rm "$DELUGE_PATH/services/router/.crossbar/node.key"
    rm "$DELUGE_PATH/services/router/.crossbar/node.pid"
}

# Watch for django test database in realtime
func_watchpsql() {
    watch -n 0.2 "psql -h dev.absortium.com -p 5432 -U postgres -d test_postgres -c '$1'"
}
alias watchpsql=func_watchpsql

# Sync time on the docker machine after sleep
func_recovertime() {
    docker-machine ssh default 'sudo ntpclient -s -h pool.ntp.org'
}
alias recovertime=func_recovertime

# stream copying folder/file from the docker machine
# Example: dmstreamcopy /mnt/sda1/var/lib/docker/volumes/dev_ethereumdata/_data ~/Downloads/blockchaindata/
func_streamcopy() {
    mkdir -p "$2"
    docker-machine ssh default "sudo -u root tar czpf - -C $1 . " | pipemeter |tar xzpf - -C $2
}
alias dmstreamcopy=func_streamcopy

# stream copying folder/file from the docker machine
# Example: dmstreamcopy /mnt/sda1/var/lib/docker/volumes/dev_ethereumdata/_data ~/Downloads/blockchaindata/
func_dprodbuild() {
    func_godd

}
alias dmstreamcopy=func_streamcopy