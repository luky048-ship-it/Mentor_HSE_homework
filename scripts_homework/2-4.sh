#!/bin/bash
if ping -c 1 "$1" &> /dev/null; then
    echo "Сервер $1 доступен"
else
    echo "Сервер $1 недоступен"
fi