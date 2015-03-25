#!/usr/bin/env python
#import paho
import paho.mqtt.client as mqtt
import time
import sys, getopt

host = "localhost"
opts, args = getopt.getopt(sys.argv[1:], "h:n:")

#client.connect (host, 1883, 60)

for op, value in opts:
    if op == "-h":
        div = int(value)
    else if op == "-n":
	num = int(value)
    else:
	pass
    
t = 1.0/div
while True:
    
    client = mqtt.Client("Client"+str(num), True)
    client.username_pw_set("client"+str(num), "123456")
    client.connect(host, 1883, 60)
    client.disconnect()
    time.sleep(t)
