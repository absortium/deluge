#!/usr/bin/env bash
# ------------------------------------
# Docker compose alias and function
# ------------------------------------


func_dcinit() {
    declare COMPOSE_MODE="$1"

    if [ -z "$COMPOSE_MODE" ]; then
        echo "Use default init mode '$DEFAULT_MODE'"
        COMPOSE_MODE="$DEFAULT_MODE"
    fi
    
    case "$COMPOSE_MODE" in
    'unit'|'integration'|'frontend')
        export CONTAINERS_TYPE="dev";;

    'testnet'|'realnet' )
        export CONTAINERS_TYPE="prod";;

    *)
        echo "Can not find any options similar to '$1'"
        break
    esac

    declare COMPOSES_PATH="$DELUGE_PATH/docker/composes"
    declare CONTAINERS_PATH="$DELUGE_PATH/docker/containers"

    export DOCKER_OVERRIDE="$COMPOSES_PATH/$COMPOSE_MODE.yml"
    export DOCKER_BASE="$CONTAINERS_PATH/$CONTAINERS_TYPE.yml"

    ideluge
}
alias dcinit=func_dcinit

func_dc() {
    if [[ -z "$DOCKER_OVERRIDE" || -z "$DOCKER_BASE" ]]
    then
        func_dcinit
    fi

    declare COMMAND=$(echo "$@" | python -c "import sys; print(sys.stdin.read().split(' ')[0])")

    if [ "$COMMAND" = "build" ]; then
        docker-compose -f "$DELUGE_PATH/docker/containers/$CONTAINERS_TYPE/build.yml" "$@"
    else
        echo "Docker base file: $DOCKER_BASE"
        echo "Docker override file: $DOCKER_OVERRIDE"
        echo "Full command: docker-compose -f $DOCKER_BASE -f $DOCKER_OVERRIDE $@"

        docker-compose -f "$DOCKER_BASE" -f "$DOCKER_OVERRIDE" "$@"
    fi
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