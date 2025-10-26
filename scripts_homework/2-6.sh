#!/bin/bash
file="$1"
last=$(md5sum "$file")
while true; do
    current=$(md5sum "$file")
    if [ "$last" != "$current" ]; then
        echo "Файл $file изменен"
        last="$current"
    fi
    sleep 1
done
