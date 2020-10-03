#!/usr/bin/env bash

is_leap_year () {
    if (($1 % 4 == 0)) && (($1 % 100 != 0)) || (($1 % 400 == 0)); then
        echo "true"
        return 0
    fi
    
    echo "false"
    return 1
}

# Ensure that the number of arguments is == 1 and also that the argument looks like an integer
if [ "${#@}" -gt 1 ] || [[ ! $1 =~ ^[0-9]+$ ]]; then
    echo "Usage: leap.sh <year>"
    exit 1
else
    is_leap_year "$1"
fi