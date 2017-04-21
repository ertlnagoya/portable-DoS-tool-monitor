#!/usr/bin/env python2

from socket import *
import sys
import os
import struct
import select
import time
import signal
import json
import datetime
import math
import requests
from elasticsearch import Elasticsearch
from elasticsearch import helpers

HOST = "0.0.0.0"
PORT = 33844 

# elasticsearch
packet_que = list()
es = Elasticsearch("localhost:9200")
URL = "http://localhost:9200"
INDEX_URL = URL + "/ping"
TYPE_URL = INDEX_URL + "/response"



def delete_index():
    """Delete an index in elastic search."""
    requests.delete(INDEX_URL)

def create_index():
    """Create an index in elastic search with timestamp enabled."""
    try:
        print("[*] creating an index in elasticsearch")
        r = requests.put(INDEX_URL)
        if "index_already_exists_exception" in r.text:
            print("[*] index already exists")
            return
        mapping = {
            "capture": {
                "properties": {             
                    "timestamp": {
                        "type": "date",
                    },
                    "delay": {
                        "type": "float",
                    },
                    "error": {
                        "type": "number",
                    },
                    "error_message": {
                        "type": "string",
                    },
                }
            }
        }
    except:
        raise Exception("Elasticsearch is not running")

def recv_until(c, delim="\n"):
    res = c.recv(1024)
    if len(res) == 0:
        return ""
    while not res[-1] == delim:
        data = c.recv(1024)
        if len(data) == 0:
            return res
        res += data
    return res

def process_data(data):
    print(data[:50] + "...")
    timestamp, delay, error, error_message = "", "", "", ""

    try:
        str_timestamp, delay, error, error_message = data.split(" ", 3)

    except Exception as e:
        return

    #elasticsearch -----------------------------------------------------------------
    try:
        float_timestamp = float(str_timestamp)
        row_timestamp=datetime.datetime.fromtimestamp(float_timestamp) - datetime.timedelta(hours=9)
        timestamp = row_timestamp.strftime("%Y-%m-%dT%H:%M:%SZ") 
        #print timestamp        
        res = es.index(index="ping", doc_type="response", body={"timestamp": timestamp, "delay": float(delay), "error": float(error), "error_message" : error_message})
       #res = es.index(index="ping", doc_type="response", body={"timestamp": timestamp, "delay": delay, "error": error, "error_message" : error_message})
        print(res)

    except Exception as e:
        print(e)
        time.sleep(1)

    #---------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------
    return 

#delete_index()
create_index()

while True:
    s = socket(AF_INET)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    print("[*] waiting for connection at %s:%s" % (HOST, PORT))
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print("[*] connection from: %s:%s" % addr)
    while True:
        payload = recv_until(conn)
        if len(payload) == 0:
            break
        process_data(payload)
        #print("waiting...")
    conn.close()    