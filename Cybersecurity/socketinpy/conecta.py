import socket

# Solicita o IP e a porta, garantindo que a porta seja convertida em um número inteiro
ip = input("Digite o IP: ")
try:
    porta = int(input("Digite a porta: "))
except ValueError:
    print("Por favor, insira um número válido para a porta.")
    exit()

# Criação do socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define um tempo limite para a conexão (opcional, para evitar esperas longas)
meusocket.settimeout(3)

# Conecta ao IP e à porta especificada, usando connect_ex para retornar um código de erro
resultado = meusocket.connect_ex((ip, porta))

# Verifica o resultado da conexão
if resultado == 0:
    print(f"Porta {porta} no IP {ip} está ABERTA.")
else:
    print(f"Porta {porta} no IP {ip} está FECHADA.")

# Fecha o socket
meusocket.close()
