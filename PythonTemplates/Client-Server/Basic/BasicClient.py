"""
Basic client side code template
https://realpython.com/python-sockets/

Ryan Flynn
"""

import socket

HOST = "127.0.0.1"      # IP of server
PORT = 65243            # Port of service


def main():
    # initialize socket connection to server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))          # bind address and port to socket
        sock.sendall(b"hello world")        # send payload to server

        data = sock.recv(1024)              # get server response

    print(f"Socket closed. Recieved msg from server: {repr(data)}")


if __name__ == '__main__':
    main()
