"""
Ryan Flynn
https://realpython.com/python-sockets/

Multiple connection server application template
"""

import selectors
import socket
import sys
import types


def accept_wrapper(sock, sel):
    """
    In basic socket programming, accept blocks and awaits
    a connection from a client. Due to the event loop
    implementation making use of the `select` syscall, accept
    should not block. This function serves as a wrapper around
    accept to bind the connection over the socket to
    the selector.

    :param sock: the server socket to service the connection
    :param sel: the selector object
    """
    conn, addr = sock.accept()                                  # Should be ready to read
    conn.setblocking(False)
    print('Accepted connection from', addr)

    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)                       # register the socket to the selector


def service_connection(sel, key, mask):
    """
    Client is connected. Now, perform server logic.
    """
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:                             # Socket ready for reading
        recv_data = sock.recv(1024)                             # Get data from socket
        if recv_data:
            data.outb += recv_data
        else:                                                   # if b'' sent, close the socket, unregister it from selector
            # Note: b'' indicates socket.close was called
            # on client side. In real client-server appl.s
            # server should time-out any unresponsive
            # connections after a period of time.
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:                            # Socket ready for writing
        if data.outb:                                           # if there's data waiting to be sent, send it
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)                         # Should be ready to write
            data.outb = data.outb[sent:]


def main():
    if len(sys.argv) != 3:
        print("usage:", sys.argv[0], "<host> <port>")
        sys.exit(1)

    _, host, port = sys.argv

    sel = selectors.DefaultSelector()

    # configure server side socket to service connections with
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((host, int(port)))
    lsock.listen()

    lsock.setblocking(False)                                    # Don't block, so service connections as they come
    sel.register(lsock, selectors.EVENT_READ, data=None)        # data stores all data transmitted to server on connection

    # Event loop
    while True:
        events = sel.select(timeout=None)                       # blocks until sockets ready to service
        for key, mask in events:
            if key.data is None:
                # accept the connection; fileobj is the socket
                accept_wrapper(key.fileobj, sel)
            else:
                service_connection(sel, key, mask)


if __name__ == '__main__':
    main()
