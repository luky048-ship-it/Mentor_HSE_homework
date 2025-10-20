#!/bin/bash

hello_func() {
    local string=$1
    echo "Hello, $string"
}

sum_func() {
    local num1=$1
    local num2=$2
    echo $((num1 + num2))
}

hello_func "World!"
result=$(sum_func 5 10)
echo "Сумма: $result"
