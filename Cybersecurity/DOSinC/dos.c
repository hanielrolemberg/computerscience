#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define PORT 80
#define REQUEST_COUNT 1000  // Número de requisições a serem enviadas

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <target_ip> <target_port>\n", argv[0]);
        return 1;
    }

    char *target_ip = argv[1];
    int target_port = atoi(argv[2]);

    int sockfd;
    struct sockaddr_in server_addr;
    char request[] = "GET / HTTP/1.1\r\nHost: target\r\nConnection: close\r\n\r\n";

    // Cria o socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("Socket creation failed");
        return 1;
    }

    // Configura o endereço do servidor
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(target_port);
    inet_pton(AF_INET, target_ip, &server_addr.sin_addr);

    for (int i = 0; i < REQUEST_COUNT; ++i) {
        // Conecta ao servidor
        if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
            perror("Connection failed");
            close(sockfd);
            return 1;
        }

        // Envia a requisição HTTP
        send(sockfd, request, strlen(request), 0);

        // Fecha a conexão
        close(sockfd);

        // Recria o socket para a próxima requisição
        sockfd = socket(AF_INET, SOCK_STREAM, 0);
        if (sockfd < 0) {
            perror("Socket creation failed");
            return 1;
        }
    }

    printf("Sent %d requests to %s:%d\n", REQUEST_COUNT, target_ip, target_port);

    close(sockfd);
    return 0;
}
