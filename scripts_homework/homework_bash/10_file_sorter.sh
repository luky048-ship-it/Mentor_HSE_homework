#!/bin/bash

dir=$1
log_file="sort_log.txt"

mkdir -p "$dir/Images" "$dir/Documents"

for file in "$dir"/*; do
    if [ -f "$file" ]; then
        ext="${file##*.}"
        if [ "$ext" = "jpg" ] || [ "$ext" = "png" ] || [ "$ext" = "gif" ]; then
            mv "$file" "$dir/Images/"
            echo "Перемещён в Images: $file" >> $log_file
        elif [ "$ext" = "txt" ] || [ "$ext" = "pdf" ] || [ "$ext" = "docx" ]; then
            mv "$file" "$dir/Documents/"
            echo "Перемещён в Documents: $file" >> $log_file
        fi
    fi
done







# Скрипт сортирует файлы в указанной директории по расширениям в папки Images и Documents, записывает лог.
