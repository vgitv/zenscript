#!/bin/bash

function title {
    col=155
    echo -e "\e[38;5;${col}m$1\e[0m"
}

function try {
    local action='retry'

    echo "=> try >>> $*"

    while [[ "${action}" = 'retry' ]]; do
        if "$@"; then
            action='ok'
            echo '=> Success'
        else
            echo "=> ERROR"
            echo '=> Continue ? ( retry / skip )'
            read -r action
            while [[ ! "${action}" =~ ^(retry|skip)$ ]]; do
                echo '=> Wrong choice ( retry / skip )'
                read -r action
            done
        fi
    done
    echo
}


function autoretry {
    local nbtry="$1"
    shift
    local cpt=0
    while [[ $cpt -lt $nbtry ]]; do
        echo "Try n°${cpt}"
        if "$@"; then
            echo 'Success!'
            return
        fi
        cpt=$((cpt+1))
        sleep 1
    done
    echo "ERROR: ${nbtry} unsuccessful tries of command '$*'"
    exit 1
}
