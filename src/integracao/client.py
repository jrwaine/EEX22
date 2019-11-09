#!/usr/bin/env python3

import socket
import json

HOST = '192.168.100.74'  # The server's hostname or IP address
PORT = 9077        # The port used by the server

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data = s.recv(1024)
            b = b''
            b += data
            d = json.loads(b.decode('utf-8'))
            print(d)
            break
    except:
        pass


