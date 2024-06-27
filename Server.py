import socket

server_address = ('localhost', 12345)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)

server_socket.listen(1)  

print(f"Servidor TCP esperando conexiones en {server_address}")

while True:
    connection, client_address = server_socket.accept()

    try:
        print(f"Conexión establecida desde {client_address}")

        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Mensaje recibido del cliente TCP: {data.decode()}")

            response = "Mensaje recibido correctamente"
            connection.sendall(response.encode())

    finally:
        connection.close()
