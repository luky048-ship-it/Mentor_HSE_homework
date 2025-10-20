#!/bin/bash

echo "Текущее значение PATH: $PATH"

if [ $# -eq 0 ]; then
    echo "Ошибка: укажите директорию как аргумент."
    exit 1
fi

new_dir=$1
export PATH="$PATH:$new_dir"
echo "Новое значение PATH: $PATH"
