"Host-to-IP Resolver in C: Converting Domain Names to IP Addresses"

# Hostname to IP Resolver in C

This C program resolves a given hostname to its corresponding IP address using the `gethostbyname` function. It outputs the first resolved IP address for the provided domain.

## How It Works

The program takes a hostname as an argument and resolves it to an IP address. If the resolution is successful, it prints the corresponding IP address. Otherwise, it prints an error message indicating that the hostname could not be resolved.

### Example:

```bash
$ ./hostname_resolver www.example.com
www.example.com ===> 93.184.216.34
```

## Usage:
Compile the code:

```bash

gcc -o hostname_resolver hostname_resolver.c
```

## Run the program:

```bash
./hostname_resolver <hostname>
```

Replace <hostname> with the actual domain name you want to resolve.