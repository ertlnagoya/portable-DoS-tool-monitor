import signal
import cv2
import base64
from os import system
from time import sleep, time
import copy
try:
    import queue
except ImportError:
    import Queue as queue
from socket import *
from sys import argv

def usage():
    print "usage: %s SERVER_IP_ADDR" % argv[0]
    exit()

if len(argv) == 1:
    usage()
HOST = argv[1]
PORT = 33843 # webam

CAPTURE_FILE_NAME = "dummy.jpg"
URL_PREFIX = "data:image/jpg;base64,"

q = queue.Queue()

def do_capture():
    time_stamp = str(time())
    with open(CAPTURE_FILE_NAME, "rb") as f:
        buf = f.read()
        buf_b64e = base64.b64encode(buf)
        URL = URL_PREFIX + buf_b64e
        q.put((time_stamp, URL))

def cyclic_task(delay, interval):
    do_capture()

def sigint_handler():
    print("[*] terminating webcam client...")
    exit()

signal.signal(signal.SIGINT, sigint_handler)
signal.signal(signal.SIGALRM, cyclic_task)
signal.setitimer(signal.ITIMER_REAL, 1, 8)

s = socket(AF_INET)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
print("[*] connecting to %s:%s" % (HOST, PORT))
s.connect((HOST, PORT))
while True:
    sleep(1)
    if not q.empty():
        time_stamp, capture = q.get()
        s.sendall(' '.join([time_stamp, capture]) + "\n")
conn.close()
