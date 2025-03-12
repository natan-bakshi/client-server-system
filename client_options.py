import socket

client = socket.socket()
client.connect(('127.0.0.1', 8800))


def get_input():
    accepted = 0
    while accepted != 1 and accepted != 2 and accepted != 3 and accepted != 4:
        accepted = int(input('''
    for time accepted press 1
    for name accepted press 2
    for random number accepted press 3
    for exit press 4
    '''))
    return accepted


def create_message(message):
    message = str(len(message)).zfill(2) + message
    return message


def main():
    while True:
        request = get_input()
        if request == 1:
            message = create_message("time")
            client.send(message.encode())
            print("The time request has been sent")

        if request == 2:
            message = create_message("name")
            client.send(message.encode())
            print("The name request has been sent")

        if request == 3:
            message = create_message("rand")
            client.send(message.encode())
            print("The random number request has been sent")

        if request == 4:
            message = create_message("exit")
            client.send(message.encode())
            print("The exit request has been sent")
            break

        len_data = client.recv(2).decode()

        try:
            data = client.recv(int(len_data)).decode()
            print("the server said: ", data)

        except ValueError:
            print("The server length field does not include integers")
        except TypeError:
            print("The server length field cannot be converted to an integer")

        if len(client.recv(1024).decode()) > 0:
            garbage = client.recv(1024).decode()


main()


