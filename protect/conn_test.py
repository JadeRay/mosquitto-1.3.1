#!/usr/bin/env python
#import paho
import paho.mqtt.client as mqtt
import time
import sys, getopt

host = "192.168.139.80"
opts, args = getopt.getopt(sys.argv[1:], "h:")

#client.connect (host, 1883, 60)

for op, value in opts:
    if op == "-h":
        d = int(value)
    
t = 1.0/d
i = 1
while True:
    client = mqtt.Client("conn_test"+str(i), True)
    client.connect(host, 1883, 60)
    time.sleep(t)
