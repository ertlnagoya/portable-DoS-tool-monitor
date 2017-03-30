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
ACTION = {"_index" : "traffics",
          "_type" : "traffic",
          "_source": {}
         }
before_timestamp = 0
before_count = 0

def delete_index():
    """Delete an index in elastic search."""
    requests.delete(INDEX_URL)

def create_index():
    """Create an index in elastic search with timestamp enabled."""
    requests.put(INDEX_URL)
    setting = {"traffic" : {
                "_timestamp" : {
                    "enabled" : True,
                    "path" : "capture_timestamp",
                },
                "numeric_detection" : False,
                },
                "properties" : {
                    "traffic":{
                        "type" : "number",
                    },
                    "attack_bandwidth":{
                        "type" : "number",
                    },
                }
            }
    for _ in range(1, 100):
        try:
            r = requests.put(TYPE_URL + "/_mapping", data=json.dumps(setting))
            break
        except:
            time.sleep(1)
            pass

def process_data(data):
    global before_count,before_timestamp
    sys.stdout.write(data)
    timestamp, count="",""

    # elasticsearch -----------------------------------------------------------------
    try:
        timestamp, count=data.split(" ")
    except Exception as e:
        return

    timestamp = float(timestamp)
    count = int(count[:-1])
    #print timestamp
    #print count
    attack_bandwidth = float(count - before_count) / (timestamp - before_timestamp)

    try:
        if before_timestamp == 0:
            before_timestamp = timestamp
            before_count = count
            return
        before_timestamp = timestamp
        before_count = count


        row_timestamp=datetime.datetime.fromtimestamp(timestamp) - datetime.timedelta(hours=9)
        print row_timestamp
        timestamp = row_timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
        #protocol = None
        parsed_packet = dict(traffic = count,attack_bandwidth = attack_bandwidth, capture_timestamp = timestamp)
        #print timestamp
        #print count
        action = ACTION.copy()
        action["_source"].update(parsed_packet)
        packet_que.append(action)    
        h=helpers.bulk(es, packet_que) #send info to ES
        #print h
        del packet_que[0:len(packet_que)]
    except Exception as e:
       time.sleep(1)
    # ------------------------------------------------------------------------------
    return 


# elasticsearch
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