import socket

def scan_ports(ip, start_port, end_port):
    for porta in range(start_port, end_port + 1):
        try:
            # Criação do socket TCP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Define um tempo limite para a conexão

            # Tenta conectar ao IP e à porta especificada
            resultado = s.connect_ex((ip, porta))

            # Verifica o resultado da conexão
            if resultado == 0:
                print(f"Porta {porta}: Aberta")
            else:
                print(f"Porta {porta}: Fechada")
        except socket.error as e:
            print(f"Erro ao conectar na porta {porta}: {e}")
        finally:
            # Garante que o socket seja fechado corretamente
            s.close()

def main():
    # Solicita o IP do alvo e a faixa de portas a serem escaneadas
    ip = input("Digite o IP do alvo: ")
    start_port = 1
    end_port = 65535
    
    print(f"Iniciando a varredura de portas no IP {ip}...")
    scan_ports(ip, start_port, end_port)
    print("Varredura concluída.")

if __name__ == "__main__":
    main()
