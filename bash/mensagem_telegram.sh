#!/bin/bash

# Substitua com as suas credenciais do Telegram
TELEGRAM_TOKEN="SEU_TOKEN_AQUI"
CHAT_ID="SEU_CHAT_ID_AQUI"

MENSAGEM="${1:-"Mensagem enviada via Shell Script!"}"

# Envio da mensagem utilizando cURL e a API do Telegram
curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage" \
    -d "chat_id=${CHAT_ID}" \
    -d "text=${MENSAGEM}" > /dev/null

if [ $? -eq 0 ]; then
    echo "Mensagem enviada com sucesso para o Telegram!"
else
    echo "Falha ao enviar mensagem."
fi