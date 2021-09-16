#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # connect to server
    while True:
        # enter the text we want to send to server
        text = str(input('write text: '))
        if text == 'exit':
            break
        s.send(text.encode())           # encode text to bytes
        data = s.recv(1024)             # get data in bytes from server
        print(data.decode())            # decode and output data from server
