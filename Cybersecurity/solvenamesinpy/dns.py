import socket
import sys

# Verifica se o nome do host foi fornecido como argumento
if len(sys.argv) != 2:
    print("Uso: python script.py <hostname>")
    sys.exit(1)

hostname = sys.argv[1]

try:
    # Resolve o nome do host para um endereço IP
    ip_address = socket.gethostbyname(hostname)
    print(f"{hostname} ===> {ip_address}")
except socket.error as e:
    print(f"Erro ao resolver {hostname}: {e}")
    sys.exit(1)


