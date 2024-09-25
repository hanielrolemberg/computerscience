#include <stdio.h>
#include <netdb.h>
#include <arpa/inet.h>

int main (int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <hostname>\n", argv[0]);
        return 1;
    }

    char *target = argv[1];  // Hostname argument
    struct hostent *host = gethostbyname(target);  // Resolve hostname to IP

    if (host == NULL) {
        printf("Error resolving hostname.\n");
        return 1;
    }

    // Print the first resolved IP address
    printf("%s ===> %s \n", target, inet_ntoa(*((struct in_addr *)host->h_addr)));

    return 0;
}
