#!/bin/bash

read -p "Primeiro número: " n1
read -p "Operação (+, -, *, /): " op
read -p "Segundo número: " n2

case "$op" in
    "+") res=$((n1 + n2)) ;;
    "-") res=$((n1 - n2)) ;;
    "*") res=$((n1 * n2)) ;;
    "/") 
        if [ "$n2" -eq 0 ]; then
            echo "Erro: Divisão por zero"
            exit 1
        fi
        res=$((n1 / n2)) 
        ;;
    *) 
        echo "Operação inválida"
        exit 1 
        ;;
esac

echo "Resultado: $res"