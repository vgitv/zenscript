#!/bin/bash

export NC="\033[0m"

export debug="\033[1;37m"
export info="\033[1;32m"
export warn="\033[1;33m"
export error="\033[1;31m"


function log {
    echo -e "${!1:?}$(date '+%Y-%m-%d %H:%M:%S') - $(printf "%-5s" "${1^^}") - ${2}${NC}"
}


function error {
    log error "$*"
    exit 1
}
