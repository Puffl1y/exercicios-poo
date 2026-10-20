#!/bin/bash

ARQUIVO="/caminho/para/o/arquivo.txt"

if [ ! -f "$ARQUIVO" ]; then
    exit 1
fi

wc -l < "$ARQUIVO"