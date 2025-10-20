#!/bin/bash

if [ -f "input.txt" ]; then
    cat input.txt
else
    echo "Файл input.txt не найден."
fi

wc -l input.txt > output.txt
echo "Вывод wc -l сохранён в output.txt."

ls non_existent_file 2> error.log
echo "Ошибки ls сохранены в error.log."
