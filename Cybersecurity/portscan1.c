#include <stdio.h>         // Biblioteca padrão de entrada e saída
#include <arpa/inet.h>     // Para inet_addr
#include <netdb.h>         // Para estruturas relacionadas a socket
#include <unistd.h>        // Para a função close

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Uso: %s <IP de destino>\n", argv[0]);
        return 1;
    }

    int meusocket, conecta;  // Variáveis para o socket e o resultado da conexão
    int port;  // Variável para iterar pelas portas
    int inicio = 0, final = 65535;  // Varredura de portas de 0 a 65535
    char *destino = argv[1];  // Endereço IP de destino (passado por argumento)

    struct sockaddr_in alvo;  // Estrutura para armazenar informações do alvo
    alvo.sin_family = AF_INET;  // Protocolo IP

    // Verifica se o IP de destino é válido
    if (inet_addr(destino) == INADDR_NONE) {
        printf("Endereço IP inválido.\n");
        return 1;
    }

    // Itera pelas portas de 'inicio' até 'final'
    for (port = inicio; port <= final; port++) {
        // Criando o socket (AF_INET = IPv4, SOCK_STREAM = TCP)
        meusocket = socket(AF_INET, SOCK_STREAM, 0);
        if (meusocket == -1) {
            printf("Erro ao criar o socket\n");
            return 1;  // Retorna 1 para indicar erro
        }

        // Configura a porta e o endereço IP do alvo
        alvo.sin_port = htons(port);  // Define a porta (convertida para big-endian)
        alvo.sin_addr.s_addr = inet_addr(destino);  // Define o endereço IP do alvo

        // Tentativa de conexão ao alvo
        conecta = connect(meusocket, (struct sockaddr *)&alvo, sizeof(alvo));

        // Verifica se a conexão foi bem-sucedida
        if (conecta == 0) {
            printf("Porta %d - status [ABERTA]\n", port);
        }

        // Fecha o socket após cada tentativa, independentemente do sucesso
        close(meusocket);
    }

    return 0;
}
