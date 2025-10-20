#!/bin/bash

cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')
mem=$(free -m | awk '/Mem/{print $3/$2 * 100}')
disk=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

echo "CPU: $cpu%"
echo "Память: $mem%"
echo "Диск: $disk%"

if [ ${mem%.*} -gt 80 ]; then
    echo "Память > 80%! Топ процессов:"
    ps -aux --sort=-%mem | head -n 3
fi








#Скрипт собирает данные о загрузке процессора, памяти и диска, и уведомляет, если использование памяти превышает 80%.
