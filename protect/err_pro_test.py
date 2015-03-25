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

client.username_pw_set("client"+str(num), "123456")

client.connect (host, 1883, 60)
topic = "/test/normal" #the right topic is /u/#
payload = "this is a test" #the right payload must begin with "AA07"
qos = 2
while True:
	client.publish(topic, payload, qos, False)
	time.sleep(t)
