#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))  # connect to server
        print('connection with server was successfull')
    except:
        print('Connection can not be complete')
        exit()
    try:
        while True:
            # enter the text we want to send to server
            text = str(input('write text: '))
            if text == 'exit':
                break
            s.send(text.encode())
            print('we are sending data!')           # encode text to bytes
            data = s.recv(1024)             # get data in bytes from server
            print('we are received data!')
            # decode and output data from server
            print(data.decode())
    except:
        print('connection was lost')
