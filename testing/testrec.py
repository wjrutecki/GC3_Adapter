import socket, json

incomingPort = 9090


rec_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

rec_socket.bind(('localhost', incomingPort))

rec_socket.listen(1)

while True:
    connection, client_address = rec_socket.accept()
    try:
        data = connection.recv(1000)
        inputMessage = data.decode()
        print(inputMessage)
    finally:
        connection.close()
