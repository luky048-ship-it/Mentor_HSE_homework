#!/bin/bash
if [ $1 -gt $2 ]; then
    echo "$1 больше $2"
elif [ $1 -lt $2 ]; then
    echo "$1 меньше $2"
else
    echo "$1 равно $2"
fi