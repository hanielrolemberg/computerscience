#include <stdio.h>         // Standard input/output library
#include <arpa/inet.h>     // For inet_addr
#include <netdb.h>         // For socket-related structures
#include <unistd.h>        // For the close function

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <Target IP>\n", argv[0]);
        return 1;
    }

    int my_socket, connection;  // Variables for the socket and connection result
    int port;  // Variable for iterating through ports
    int start_port = 0, end_port = 65535;  // Scanning ports from 0 to 65535
    char *target_ip = argv[1];  // Target IP address (passed as an argument)

    struct sockaddr_in target;  // Structure to store target information
    target.sin_family = AF_INET;  // IP protocol

    // Check if the target IP is valid
    if (inet_addr(target_ip) == INADDR_NONE) {
        printf("Invalid IP address.\n");
        return 1;
    }

    // Iterate through ports from 'start_port' to 'end_port'
    for (port = start_port; port <= end_port; port++) {
        // Create the socket (AF_INET = IPv4, SOCK_STREAM = TCP)
        my_socket = socket(AF_INET, SOCK_STREAM, 0);
        if (my_socket == -1) {
            printf("Error creating the socket\n");
            return 1;  // Return 1 to indicate an error
        }

        // Configure the port and IP address of the target
        target.sin_port = htons(port);  // Set the port (converted to big-endian)
        target.sin_addr.s_addr = inet_addr(target_ip);  // Set the target IP address

        // Attempt to connect to the target
        connection = connect(my_socket, (struct sockaddr *)&target, sizeof(target));

        // Check if the connection was successful
        if (connection == 0) {
            printf("Port %d - status [OPEN]\n", port);
        }

        // Close the socket after each attempt, regardless of success
        close(my_socket);
    }

    return 0;
}
