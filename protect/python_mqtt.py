#!/usr/bin/env python
#import paho
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print ("Connected with result code "+ str(rc))
	
#	client.subscribe("$SYS/broker/load/protect/#")
	client.subscribe("$SYS/broker/load/#")
	client.subscribe("/test/happy")
	

def on_message(client, userdata, msg):
	print (msg.topic + " " + str(msg.payload))
	

client = mqtt.Client("python_client", True)
client.on_connect = on_connect
client.on_message = on_message

host = "127.0.0.1"

client.connect (host, 1883, 60)

client.loop_forever()
