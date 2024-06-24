import socket

server_address = ('localhost', 12345)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(server_address)

print(f"Servidor UDP esperando conexiones en {server_address}")

while True:
    data, client_address = server_socket.recvfrom(1024)

    print(f"Mensaje recibido del cliente UDP: {data.decode()}")

    response = "Mensaje recibido correctamente"
    server_socket.sendto(response.encode(), client_address)
