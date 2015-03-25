#!/usr/bin/env python
#import paho
import paho.mqtt.client as mqtt
import time
import sys, getopt


opts, args = getopt.getopt(sys.argv[1:], "h:n:")

for op, value in opts:
    if op == "-h":
        div = int(value)
    else if op == "-n":
	num = int(value)
    else:
	pass

t = 1.0/div

client = mqtt.Client("Client"+str(num), True)
host = "localhost"

client.connect (host, 1883, 60)
topic = "/test/happy" #the right topic is /u/#
payload = "A3B3 happy" #the right payload must begin with "A3B3"
qos = 2
while True:
    client.publish(topic, payload, qos, False)
    time.sleep(t)
