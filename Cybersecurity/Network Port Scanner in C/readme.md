# TCP Port Scanner in C

This project is a basic TCP port scanner written in C. The scanner attempts to connect to a target IP address and checks if TCP ports are open by iterating over a range of ports (from 0 to 65535).

## Features

- Scans all available TCP ports (0 to 65535).
- Identifies open ports by attempting to establish a TCP connection.
- Simple and fast implementation using socket programming in C.

## How It Works

The program takes a target IP address as input and tries to establish a TCP connection on each port. If the connection is successful, it reports the port as open. If not, it moves on to the next port. The program uses raw sockets and the `connect()` system call to check the status of each port.

### Prerequisites

- C Compiler (e.g., GCC)
- A terminal or command line interface to run the program.

### How to Compile

To compile the program, use a C compiler like `gcc`:

```bash
gcc portscanner.c -o portscanner
```

## How to Run
After compiling, you can run the program by providing the target IP address as a command-line argument. Example:

```bash
127.0.0.1
```
Note: It's your localhost.