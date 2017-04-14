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

CAPTURE_FILE_NAME = "capture.jpg"
URL_PREFIX = "data:image/jpg;base64,"
q = queue.Queue()
cap = cv2.VideoCapture(1)#mac   #cap = cv2.VideoCapture(0)
if cap.isOpened() is False:
    raise("Camera IO Error")

def compare_capture(cap1, cap2):
    cap1_hist = cv2.calcHist([cap1], [0], None, [256], [0, 256])
    cap2_hist = cv2.calcHist([cap2], [0], None, [256], [0, 256])
    ret = cv2.compareHist(cap1_hist, cap2_hist, 0)
    return ret

prev_frame = None
def do_capture():
    global prev_frame
    time_stamp = str(time())
    ret, frame = cap.read()
    if ret == False:
        raise("capture failed")

    if not prev_frame == None:
        if compare_capture(prev_frame, frame) >= 0.8:
            return

    prev_frame = copy.deepcopy(frame)
    cv2.imwrite(CAPTURE_FILE_NAME, frame)
    cv2.imwrite("./seq/" + str(int(time())) + ".jpg", frame)
    with open(CAPTURE_FILE_NAME, "rb") as f:
        buf = f.read()
        buf_b64e = base64.b64encode(buf)
        URL = URL_PREFIX + buf_b64e
        q.put((time_stamp, URL))
        # with open("URL.txt", "w") as fw:
        #     fw.write(URL)
        # system("firefox " + URL.replace(';', '\;') + buf_b64e)

def cyclic_task(delay, interval):
    do_capture()

def sigint_handler():
    global cap
    print("[*] terminating webcam client...")
    cap.release()
    exit()

signal.signal(signal.SIGINT, sigint_handler)
signal.signal(signal.SIGALRM, cyclic_task)
signal.setitimer(signal.ITIMER_REAL, 1, 1)

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