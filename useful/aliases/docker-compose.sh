#!/usr/bin/env bash
# ------------------------------------
# Docker compose alias and function
# ------------------------------------


func_dcinit() {
    declare DELUGE_MODE="$1"

    if [ -z "$DELUGE_MODE" ]; then
        echo "Use default init mode '$DEFAULT_MODE'"
        DELUGE_MODE="$DEFAULT_MODE"
    fi
    
    case "$DELUGE_MODE" in
    'unit' )
        export DOCKER_OVERRIDE="unit.yml"
        export DOCKER_BASE="base-dev.yml";;

    'integration' )
        export DOCKER_OVERRIDE="integration.yml"
        export DOCKER_BASE="base-dev.yml";;
    'testnet' )
        export DOCKER_OVERRIDE="testnet.yml"
        export DOCKER_BASE="base-prod.yml";;

    'frontend' )
        export DOCKER_OVERRIDE="frontend.yml"
        export DOCKER_BASE="base-dev.yml";;
    *)
        echo "Can not find any options similar to '$1'"
    esac
}
alias dcinit=func_dcinit

# docker-compose alias
func_dc() {
    if [[ -z "$DOCKER_OVERRIDE" || -z "$DOCKER_BASE" ]]
    then
        func_dcinit
    fi

    # Go the docker directory
    godd

    echo "Docker base file: $DOCKER_BASE"
    echo "Docker override file: $DOCKER_OVERRIDE"
    echo "Full command: docker-compose -f $DOCKER_BASE -f $DOCKER_OVERRIDE $@"
    docker-compose -f "$DOCKER_BASE" -f "$DOCKER_OVERRIDE" "$@"
}
alias dc=func_dc

# docker-compose run alias
alias dcr="dc run"

# docker-compose up alias
alias dcu="dc up"

# docker-compose run alias
alias dcl="dc logs"

# docker-compose run alias
alias dcb="dc build"