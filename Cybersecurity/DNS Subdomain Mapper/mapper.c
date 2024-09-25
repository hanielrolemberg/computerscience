#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <arpa/inet.h>

#define MAX_LEN 256  // Tamanho máximo para subdomínio + domínio

void resolve_domain(char *domain) {
    struct hostent *host = gethostbyname(domain);
    if (host != NULL) {
        printf("%s ===> %s \n", domain, inet_ntoa(*((struct in_addr *)host->h_addr)));
    } else {
        printf("%s could not be resolved.\n", domain);
    }
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <domain> <subdomains_file>\n", argv[0]);
        return 1;
    }

    char *domain = argv[1];
    char *subdomains_file = argv[2];
    FILE *file = fopen(subdomains_file, "r");
    if (file == NULL) {
        printf("Error opening file: %s\n", subdomains_file);
        return 1;
    }

    char subdomain[100];  // Subdomínio lido do arquivo
    char full_domain[MAX_LEN];  // Domínio completo

    // Leitura de cada linha do arquivo de subdomínios
    while (fgets(subdomain, sizeof(subdomain), file)) {
        // Remove nova linha (\n) do final da string
        subdomain[strcspn(subdomain, "\n")] = 0;

        // Concatena subdomínio com domínio principal
        snprintf(full_domain, sizeof(full_domain), "%s.%s", subdomain, domain);

        // Resolve o domínio concatenado
        resolve_domain(full_domain);
    }

    fclose(file);
    return 0;
}
