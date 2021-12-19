"""
Basic server side code template
https://realpython.com/python-sockets/

Ryan Flynn
"""

import socket

HOST = "127.0.0.1"      # Localhost
PORT = 65243            # Use ports > 1023


def main():

    # Using with here automatically closes sock at end of sequence
    # AF_INET is IPv4, so if HOST is an IP address it should be in IPv4 format
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()   # listen for client connections

        conn, addr = sock.accept()  # blocking

        # Once connected, start server side logic
        with conn:
            # NOTE: conn is a NEW socket. all recv and send operations
            # here on out belong to the conn socket, not sock. sock is never a connected socket (with syn/ack)
            print(f"Connected by {addr}")
            while True:
                # Get data transferred over the socket
                data = conn.recv(1024)
                if not data:
                    break

                # send message back over socket
                conn.sendall(data)


if __name__ == '__main__':
    main()
