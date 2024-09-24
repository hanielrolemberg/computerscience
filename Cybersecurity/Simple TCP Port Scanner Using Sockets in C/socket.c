#include <stdio.h>         // Standard input/output library
#include <arpa/inet.h>     // For inet_addr function
#include <netdb.h>         // For socket structures
#include <unistd.h>        // For the close function

int main() {
    int my_socket;
    int connection_status;  // Variable to store the connection status

    struct sockaddr_in target;  // Structure to hold target information

    // Creating the socket (AF_INET = IPv4, SOCK_STREAM = TCP)
    my_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (my_socket == -1) {
        printf("Error creating the socket\n");
        return 1;  // Return 1 to indicate an error
    }

    // Setting up the target address
    target.sin_family = AF_INET;                    // IP protocol
    target.sin_port = htons(80);                    // Port 80
    target.sin_addr.s_addr = inet_addr("192.168.0.1"); // Target IP address (ex.: your router)

    // Trying to connect to the target
    connection_status = connect(my_socket, (struct sockaddr *)&target, sizeof(target));

    if (connection_status == 0) {
        printf("Port Open\n");
    } else {
        perror("Error connecting");
    }

    // Closing the socket after the test
    close(my_socket);

    return 0;
}
