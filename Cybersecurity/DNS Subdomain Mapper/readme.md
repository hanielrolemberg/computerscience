"DNS Subdomain Mapper: Automating Subdomain Discovery for Websites"

# DNS Subdomain Mapper

## Description

The **DNS Subdomain Mapper** is a simple command-line tool written in C for discovering subdomains associated with a given domain. The program takes a list of common subdomains and checks if they are valid for the specified domain, allowing you to map out subdomains that may be used by the target website.

## Features

- **Subdomain Enumeration**: Automatically tests a list of common subdomains against a target domain.
- **DNS Resolution**: Uses DNS to resolve subdomains and display their IP addresses.
- **Customizable**: Easily modify the list of subdomains to suit specific needs or use cases.

## Requirements

- GCC or any C compiler
- Standard C library

## Usage

1. **Compile the Program**:

    ```bash
    gcc mapper.c -o mapper
    ```

2. **Run the Program**:

    ```bash
    ./mapper example.com 
    ```

    Replace `example.com` with the domain you want to test. The program will attempt to resolve common subdomains for the specified domain and print out any that are found.

## Example

```bash
./subdomain_mapper example.com
```
## Output
```diff
www.example.com ===> 93.184.216.34
mail.example.com ===> 93.184.216.34
ftp.example.com ===> No address found
```

