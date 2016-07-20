#!/usr/bin/env bash

declare BRANCH="development"

while getopts "b:" option; do
    case "$option" in
        b) BRANCH="${OPTARG}" ;;
        ?) echo "error: option -$OPTARG is not implemented"; exit ;;
    esac
done

# remove the options from the positional parameters
shift $(( OPTIND - 1 ))

git submodule foreach git pull origin "$BRANCH"