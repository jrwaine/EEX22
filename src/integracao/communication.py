#!/usr/bin/env python3

import socket
import globals
import time

class Communication:
    def __init__(self):
        print('Criando comunicacao...')   

    def try_comunication(self, data):
        init_time = time.time()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((globals.HOST, globals.PORT))
            while time.time() - init_time < globals.COMMUNICATION_LIMIT_TIME:
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Conectado por', addr)
                    conn.sendall(data)