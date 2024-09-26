#!/bin/sh

# Caminho para o arquivo de log padrão
LOG_FILE="apache_server.log"

# Função para exibir uma mensagem de uso
usage() {
    echo "Uso: $0 [opções]"
    echo "Opções:"
    echo "  -l FILE    Caminho para o arquivo de log (padrão: apache_server.log)"
    echo "  -h         Exibir esta mensagem de ajuda"
    exit 1
}

# Função para contar ocorrências e exibir o resultado
count_occurrences() {
    local pattern="$1"
    local description="$2"
    local count=$(grep -E "$pattern" "$LOG_FILE" | wc -l)
    if [ "$count" -gt 0 ]; then
        echo "$description: $count"
    fi
}

# Processa argumentos de linha de comando
while getopts ":l:h" opt; do
    case $opt in
        l )
            LOG_FILE=$OPTARG
            ;;
        h )
            usage
            ;;
        \? )
            echo "Opção inválida: -$OPTARG" 1>&2
            usage
            ;;
        : )
            echo "Opção -$OPTARG requer um argumento." 1>&2
            usage
            ;;
    esac
done
shift $((OPTIND -1))

# Verifica se o arquivo de log existe
if [ ! -f "$LOG_FILE" ]; then
    echo "Arquivo de log não encontrado: $LOG_FILE"
    exit 1
fi

echo "Analisando o arquivo de log: $LOG_FILE"
echo "==============================="

# Detecção de tentativas específicas
count_occurrences "' OR '1'='1" "Tentativas de SQL Injection"
count_occurrences "/etc/passwd|/admin/config.php|/phpmyadmin/index.php" "Tentativas de acessar arquivos críticos"
count_occurrences "/admin/|/wp-login.php" "Tentativas de acessar diretórios de administração"
count_occurrences "POST /login HTTP/1.1\" (403|302)" "Tentativas de login com falha"
count_occurrences "/robots.txt" "Tentativas de scan de vulnerabilidade"
count_occurrences "500|curl" "Outras ações suspeitas (500 errors, curl requests)"

echo "==============================="
echo "Análise completa."
