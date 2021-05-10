import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 4000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
def game(connection, client_address):
    try:
        while True:
            msg = connection.recv(4096)
            print(f"Client's turn{msg.decode('utf-8')}, from{client_address}")
            connection.sendall(msg)
    finally:
        connection.close()

sock.listen(5)

try:

    message = b'Start game. It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(4096)
        amount_received += len(data)
        print('received {!r}'.format(data))


finally:
    print('closing socket')
    sock.close()
