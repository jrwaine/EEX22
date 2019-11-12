#!/usr/bin/env python3

import socket
import json
import time
import globals

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((globals.HOST, globals.PORT))
            data = s.recv(1024)
            b = b''
            b += data
            d = json.loads(b.decode('utf-8'))
            print(d)
            break
    except:
        print("conectando ao servidor...aguarde")
        time.sleep(5)
        pass


