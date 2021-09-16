#!/usr/bin/env python3

import socket
print('server is starting')


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))    # bind our socket to the given host and port
    while True:
        command = input()
        if command == 'listen':
            s.listen()
        elif command == 'off':
            break
        print('port is listened')
        conn, addr = s.accept()  # new socket and client address
        print('connection was successfull')
        with conn:
            while True:
                data = conn.recv(1024)
                if data:
                    print('i got data!')
                else:
                    print('client was disconnected')
                    break
                data = data.decode().upper()  # change text
                data = data.encode()
                conn.send(data)
                print('data was sent')

    print('server was turned off')
