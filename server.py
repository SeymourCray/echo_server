#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))    # bind our socket to the given host and port
    s.listen()
    conn, addr = s.accept()  # new socket and client address
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if data:
                print('i got data!')
            if not data:
                break
            data = data.decode().upper()  # change text
            data = data.encode()
            conn.send(data)
