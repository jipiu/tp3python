import socket

server_address = ('127.0.0.1', 12345)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    message = "Hola, servidor UDP"
    client_socket.sendto(message.encode(), server_address)

    data, server = client_socket.recvfrom(1024)
    print(f"Respuesta del servidor UDP: {data.decode()}")

finally:
    client_socket.close()
