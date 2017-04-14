#!/usr/bin/env python2

from socket import *
import sys
import time

HOST = "0.0.0.0"
PORT = 37133

while True:
    s = socket(AF_INET)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        payload = conn.recv(128)
        if len(payload) > 0:
            ts = time.time()
            print("t2 = %.6f" % ts)
            conn.send("%f\n" % ts)
        else:
            break
    conn.close()