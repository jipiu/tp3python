import socket

server_address = ('127.0.0.1', 12345)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(server_address)

    message = "Hola, servidor TCP"
    client_socket.send(message.encode())

    data = client_socket.recv(1024)
    print(f"Respuesta del servidor TCP: {data.decode()}")


except Exception as e:
    print(f"Error al enviar/recibir datos: {e}")

#finally:
    #client_socket.close()
