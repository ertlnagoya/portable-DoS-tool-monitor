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
PORT = 33843 # webcam

# elasticsearch
packet_que = list()
es = Elasticsearch("localhost:9200")
URL = "http://localhost:9200"
INDEX_URL = URL + "/captures"
TYPE_URL = INDEX_URL + "/capture"

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
                    "capture": {
                        "type": "string",
                    },
                }
            }
        }
        r = requests.put(TYPE_URL + "/_mapping", data=json.dumps(mapping))
        print(r.text)
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
    timestamp, capture = "", ""

    # elasticsearch -----------------------------------------------------------------
    try:
        timestamp, capture = data.split(" ", 1)
    except Exception as e:
        return

    timestamp = float(timestamp)

    try:
        row_timestamp=datetime.datetime.fromtimestamp(timestamp) - datetime.timedelta(hours=9)
        timestamp = row_timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
        res = es.index(index="captures", doc_type="capture", body={"timestamp": timestamp, "capture": capture})
        print(res)

        res = es.search(index="captures", body={"query": {"match_all": {}}})
        print("Got %d Hits:" % res['hits']['total'])
    except Exception as e:
        print(e)
        time.sleep(1)
    # ------------------------------------------------------------------------------
    return 

# delete_index()
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