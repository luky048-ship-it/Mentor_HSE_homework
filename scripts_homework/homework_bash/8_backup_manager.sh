#!/bin/bash

dir=$1
date=$(date +%Y-%m-%d)
log_file="backup_log.txt"
count=0

for file in "$dir"/*; do
    if [ -f "$file" ]; then
        cp "$file" "${file}_${date}"
        echo "Скопирован: $file" >> $log_file
        count=$((count + 1))
    fi
done

echo "Скопировано $count файлов" >> $log_file
echo "Готово: $count файлов скопировано."







# Скрипт создаёт резервные копии файлов в указанной директории с добавлением текущей даты к именам и записывает лог в файл.
