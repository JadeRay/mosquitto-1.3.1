#!/usr/bin/env python
#import paho
import paho.mqtt.client as mqtt
import time
import sys, getopt


client = mqtt.Client("python_client_test", True)
host = "192.168.139.80"

opts, args = getopt.getopt(sys.argv[1:], "h:")

client.connect (host, 1883, 60)

for op, value in opts:
    if op == "-h":
        d = int(value)
    
t = 10.0/d

topic = "/u/happy" #the right topic is /u/#
payload = "AA07 this is a test" #the right payload must begin with "AA07"
qos = 1
while True:
    client.publish(topic, payload, qos, False)
	time.sleep(t)
