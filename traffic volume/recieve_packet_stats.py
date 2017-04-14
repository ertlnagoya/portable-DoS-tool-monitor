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
PORT = 31337

# elasticsearch
packet_que = list()
es = Elasticsearch()
URL = "http://localhost:9200"
INDEX_URL = URL + "/traffics"
TYPE_URL = INDEX_URL + "/traffic"

before_timestamp = 0
before_traffic = 0

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
                    "traffic": {
                        "type": "number",
                    },
                    "attack bandwidth": {
                        "type": "number",
                    },
                }
            }
        }

    except:
        raise Exception("Elasticsearch is not running")

       



def process_data(data):
    global before_traffic, before_timestamp
    sys.stdout.write(data)
    timestamp, traffic="",""

    # elasticsearch -----------------------------------------------------------------
    try:
        timestamp, traffic=data.split(" ")
    except Exception as e:
        return

    timestamp = float(timestamp)
    traffic = int(traffic[:-1])
    attack_bandwidth = float(traffic - before_traffic) / (timestamp - before_timestamp) 

    try:
        if before_timestamp == 0:
            before_timestamp = timestamp
            before_traffic = traffic
            return
        before_timestamp = timestamp
        before_traffic = traffic

        row_timestamp=datetime.datetime.fromtimestamp(timestamp) - datetime.timedelta(hours=9)
        timestamp = row_timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
        print timestamp
        res = es.index(index="traffics", doc_type="traffic", body={"timestamp": timestamp, "traffic": traffic, "attack bandwidth": attack_bandwidth})
        print res

        #parsed_packet = dict(traffic = count,attack_bandwidth = attack_bandwidth, capture_timestamp = timestamp)
        #action = ACTION.copy()
        #action["_source"].update(parsed_packet)
        #packet_que.append(action)    
        #h=helpers.bulk(es, packet_que) #send info to elasticsearch
        #del packet_que[0:len(packet_que)]
    except Exception as e:
        time.sleep(1)
    # ------------------------------------------------------------------------------
    return 


delete_index()
create_index()

while True:
    s = socket(AF_INET)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print conn
    while True:
        payload = conn.recv(1024)
        if len(payload) == 0:
            break
        process_data(payload)
        #print("waiting...")

    conn.close()

    