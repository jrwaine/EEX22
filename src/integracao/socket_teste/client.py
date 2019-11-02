#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    a = input()
    # while a != '-1':
    #     s.sendall(a.encode())
    #     data = s.recv(1024)
    #     print('Received', repr(data))
    #     a = input()

    data = s.recv(1024)
    while data or a != '-1':
        s.sendall(a.encode())
        data = s.recv(1024)
        print('Received', repr(data))
        a = input()



    