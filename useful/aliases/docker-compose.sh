#!/usr/bin/env bash
# ------------------------------------
# Docker compose alias and function
# ------------------------------------


func_dcinit() {
    case '$1' in
    'unit' )
        export DOCKER_OVERRIDE="unit.yml" ;;
    'integration' )
        export DOCKER_OVERRIDE="integration.yml" ;;
    'testnet' )
        export DOCKER_OVERRIDE="testnet.yml" ;;
    'frontend' )
        export DOCKER_OVERRIDE="frontend.yml" ;;
    *)
        echo "Can not find any options similar to '$1', use default $DEFAULT_MODE"
        export DOCKER_OVERRIDE="$DEFAULT_MODE.yml"
    esac

    export DOCKER_BASE="base.yml"
}
alias dcinit=func_dcinit

# docker-compose alias
func_dc() {
    if [[ -z "$DOCKER_OVERRIDE" || -z "$DOCKER_BASE" ]]
    then
        func_dcinit
    fi

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