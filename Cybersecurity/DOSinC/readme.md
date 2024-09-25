# Simple DoS Attack Tool in C

This is a basic implementation of a Denial of Service (DoS) attack tool written in C. This tool is intended solely for educational purposes to help understand the principles behind DoS attacks and network programming. 

**Important: This software is provided for educational purposes only. Using this tool to attack systems without permission is illegal and unethical. Please always ensure you have explicit permission before conducting any security testing.**

## Overview

This DoS tool sends a large number of connection requests to a specified target IP address and port. It is designed to simulate a basic network flood to help understand how DoS attacks can overwhelm network services.

## Features

- **Floods** the target with connection requests.
- **Configurable target IP address** and **port**.
- **Customizable number** of requests.

## Prerequisites

To compile and run this tool, you need:

- A C compiler (like `gcc`).
- Basic knowledge of network programming in C.
- Explicit permission to test on the target system.

## Compilation

To compile the code, use the following command:

```bash
gcc -o dos dos.c
```
