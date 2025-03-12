import socket
import random
from datetime import datetime

my_server = socket.socket()
my_server.bind(('0.0.0.0', 8800))

my_server.listen()
print("Server is up and running")

(client_socket, client_address) = my_server.accept()
print("Client connected")


def output(call):
    reply = "Your request is not defined"
    if call == "time":
        reply = str(datetime.now())
    if call == "name":
        reply = "Natan's server"
    if call == "rand":
        reply = str(random.randint(1, 10))
    if call == "exit":
        client_socket.close()
        my_server.close()
    return reply


while True:
    len_data = client_socket.recv(2).decode()

    try:
        data = client_socket.recv(int(len_data)).decode()
        print("Client sent: " + data)
        response = output(data)
        if data == "exit":
            break

    except ValueError:
        response = "The client length field does not include integers"
    except TypeError:
        response = "The client length field cannot be converted to an integer"

    if response == "Your request is not defined":
        garbage = client_socket.recv(1024).decode()

    response = str(len(response)).zfill(2) + response
    client_socket.send(response.encode())

