#!/bin/bash
while true; do
    read -p "Введите команду: " cmd
    case "$cmd" in
        "Дата") date ;;
        "Выход") exit ;;
        *) echo "Неизвестная команда. Доступные: Дата, Выход" ;;
    esac
done