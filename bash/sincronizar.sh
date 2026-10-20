#!/bin/bash

ORIGEM="/caminho/para/diretorio_origem"
DESTINO="/caminho/para/diretorio_destino"

if [ ! -d "$ORIGEM" ]; then
    exit 1
fi

mkdir -p "$DESTINO"

rsync -av --delete "$ORIGEM/" "$DESTINO/"