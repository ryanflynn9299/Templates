"""
Ryan Flynn
Multi connection client

https://realpython.com/python-sockets/

Command Line:
    python client.py host port connections
"""

import socket
import selectors
import sys
from types import SimpleNamespace

messages = [b'Message 1 from client.', b'Message 2 from client.']


def start_connections(sel, host, port, num_conns):
    server_addr = (host, port)

    for i in range(0, num_conns):
        print(f'starting connection {i + 1} to {server_addr}')

        # Set up client socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)                                    # connect would complain of non-blocking nature

        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = SimpleNamespace(connid=(i + 1),
                               msg_total=sum(len(m) for m in messages),
                               recv_total=0,
                               messages=list(messages),
                               outb=b'')
        sel.register(sock, events, data=data)


def service_connection(sel, key, mask):
    """
    Client logic once connected to server.
    :param sel:
    :param key:
    :param mask:
    :return:
    """
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:                         # Socket ready for reading
        recv_data = sock.recv(1024)                         # Get data from socket
        if recv_data:
            print(f'Received {repr(recv_data)} from connection {data.connid}')
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:  # if nothing received or everything received that was expected, close the socket, unregister it from selector
            print(f'closing connection {data.connid}')
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:                        # Socket ready for writing
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0)
        if data.outb:                                       # if there's data waiting to be sent, send it
            print(f'echoing {repr(data.outb)} to {data.connid}')
            sent = sock.send(data.outb)                     # Should be ready to write
            data.outb = data.outb[sent:]


def main():
    if len(sys.argv) != 4:
        print("usage:", sys.argv[0], "<host> <port> <num_connections>")
        sys.exit(1)

    host, port, num_conns = sys.argv[1:4]
    sel = selectors.DefaultSelector()
    start_connections(sel, host, int(port), int(num_conns))

    try:
        while True:
            events = sel.select(timeout=1)
            if events:
                for key, mask in events:
                    service_connection(sel, key, mask)
            # Check for a socket being monitored to continue.
            if not sel.get_map():
                break
    except KeyboardInterrupt:
        print("Keyboard interrupt, exiting.")
    finally:
        sel.close()


if __name__ == '__main__':
    main()
