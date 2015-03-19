#!/usr/bin/env python
#import paho
import paho.mqtt.client as mqtt
import time
import sys, getopt

host = "localhost"
opts, args = getopt.getopt(sys.argv[1:], "h:")

#client.connect (host, 1883, 60)

for op, value in opts:
    if op == "-h":
        d = int(value)
    
t = 10/d
while True:
    client = mqtt.Client("conn_test", True)
    client.username_pw_set("neo", "123456")
    client.connect(host, 1883, 60)
    client.disconnect()
    time.sleep(t)
