#!/bin/bash

echo "Список файлов в текущей директории:"
for item in *; do
    if [ -f "$item" ]; then
        type="файл"
    elif [ -d "$item" ]; then
        type="каталог"
    else
        type="другой тип"
    fi
    echo "$item - $type"
done

if [ $# -eq 0 ]; then
    echo "Ошибка: укажите файл как аргумент."
    exit 1
fi

file_to_check=$1
if [ -e "$file_to_check" ]; then
    echo "Файл $file_to_check существует."
else
    echo "Файл $file_to_check не существует."
fi

echo "Информация о файлах:"
for file in *; do
    permissions=$(ls -l "$file" | awk '{print $1}')
    echo "Файл: $file, Права: $permissions"
done
