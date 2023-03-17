#!/bin/bash
set -euo pipefail

function title {
    col=155
    echo -e "\e[38;5;${col}m$1\e[0m"
}

function try {
    local action='retry'

    echo '# --------------------------------'
    echo "# $*"

    while [[ "${action}" = 'retry' ]]; do
        if "$@"; then
            echo 'OK'
        else
            echo "ERREUR"
            echo 'Continue ? ( retry / skip )'
            read -r action
            while [[ ! "${action}" =~ (retry|skip) ]]; do
                echo 'Wrong choice ( retry / skip )'
                read -r action
            done
        fi
    done
    echo
}
