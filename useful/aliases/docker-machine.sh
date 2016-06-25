#!/usr/bin/env bash

# docker-machine run alias
alias dm="docker-machine"

# initialize docker machine, it could be default(local) or aws machine.
func_dminit() {
    eval $(docker-machine env "$1")
}
alias dminit=func_dminit
