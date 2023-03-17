#!/bin/bash
set -euo pipefail

function title
{
    col=155
    echo -e "\e[38;5;${col}m$1\e[0m"
}
