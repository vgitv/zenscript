#!/bin/bash

function dfhome {
    local s="$(df -h --output=used,size,pcent . | awk '/^\s*[0-9]/{ print $1 "/" $2 " (" $3 ")" }')"
    printf '%b' "\u2302 ${s}"
}

function volume {
    if amixer get Master | grep '\[on\]$' > /dev/null 2> /dev/null ; then
        # local prefix='🔉'
        local prefix='\U0001F50A'
        local volume="$(amixer get Master | grep -oE "[0-9]*%")"
    else
        # local prefix='🔇'
        local prefix='\U0001F507'
        local volume='off'
    fi

    echo -n "${prefix} $(printf '%4b' "${volume}")"
}

function datetime {
    echo -n "$(date +'%d/%m/%Y %H:%M')"
}

function temperature {
    local temp="$(sensors | awk '/^temp1/ { print $2 }' | tail -n 1)"
    printf '%b' "\U1F321 ${temp}"
}

function ram {
    local usedMem="$(free -h | awk '/^Mem/ { print $3 "/" $2 }')"
    printf '%b' "\U1f4bf ${usedMem}"
}
