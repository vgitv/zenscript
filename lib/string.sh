#!/bin/bash

function sanitize {
    # lower case, ascii compatible
    echo "${1,,}" | sed -E \
        -e 's/œ/oe/g' \
        -e 's/ç/c/g' \
        -e 's/[áàäâ]/a/g' \
        -e 's/[éèëê]/e/g' \
        -e 's/[íìïî]/i/g' \
        -e 's/[óòöô]/o/g' \
        -e 's/[úùüû]/u/g' \
        -e 's/\s+/-/g' \
        -e 's/[^a-z0-9]/-/g' \
        -e 's/-+/-/g'
}
