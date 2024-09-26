#!/bin/bash

# Verifica se o domínio foi passado como argumento
if [ -z "$1" ]; then
  echo "Uso: $0 dominio.com"
  exit 1
fi

DOMINIO=$1
WORDLIST="subdomains.txt"

# Verifica se o arquivo de subdomínios existe
if [ ! -f "$WORDLIST" ]; then
  echo "Arquivo $WORDLIST não encontrado!"
  exit 1
fi

echo "Procurando hosts no domínio: $DOMINIO"

# Lê cada linha do arquivo de subdomínios
while read SUBDOMINIO; do
  # Resolve o subdomínio utilizando o comando 'host'
  RESOLUCAO=$(host "$SUBDOMINIO.$DOMINIO")
  
  # Verifica se o comando 'host' retornou uma resposta válida
  if [[ "$RESOLUCAO" == *"has address"* ]]; then
    echo "Host encontrado: $RESOLUCAO"
  fi
done < "$WORDLIST"

echo "Busca finalizada."
