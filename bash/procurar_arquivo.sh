#!/bin/bash

read -p "Informe o caminho do diretório: " DIRETORIO
read -p "Informe a extensão desejada (ex: txt, log): " EXTENSAO

if [ -d "$DIRETORIO" ]; then
    echo "Buscando arquivos .$EXTENSAO em '$DIRETORIO':"
    find "$DIRETORIO" -type f -name "*.$EXTENSAO"
else
    echo "Erro: O diretório '$DIRETORIO' não existe."
fi