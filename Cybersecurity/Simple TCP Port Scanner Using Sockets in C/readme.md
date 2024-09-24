# Simple TCP Port Scanner Using Sockets in C

This project demonstrates how to create a simple TCP port scanner using sockets in C. The code attempts to connect to a specific IP address and port, reporting whether the port is open or closed. This can be useful for testing network configurations or diagnosing connectivity issues.

## Features
- Connects to a specific IP address and port using a socket.
- Checks if the target port is open or closed.
- Uses basic socket functions such as `socket()`, `connect()`, and `close()`.
- Prints an appropriate message based on the connection status.

## How It Works
The program creates a TCP socket and attempts to connect to a specified IP address and port. If the connection is successful, it reports the port as open; otherwise, it reports the port as closed.

### Example:
The current code is configured to check if port 80 (HTTP) is open on the IP address `192.168.0.1` (a typical router IP).

## Prerequisites

- **Operating System**: Linux or Unix-based system (for socket programming).
- **C Compiler**: GCC or any other C compiler.

## How to Compile

To compile the code, you can use the following command:

```bash
gcc socket.c -o socket
```

## How to Run
Once compiled, you can run the program as follows:

```bash
./socket
```

## Note
If port 80 on the specified IP address is open, you will see:
Port Open

Otherwise, the following message will appear:
Error connecting: Connection refused