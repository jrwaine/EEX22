#!/usr/bin/env python3

import socket
import globals
import time
import json

init_time = time.time()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(socket.gethostname())
    s.bind((socket.gethostname(), globals.PORT))
    while time.time() - init_time < globals.COMMUNICATION_LIMIT_TIME:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Conectado por', addr)
            conn.sendall(json.dumps('data').encode('utf-8'))
            break