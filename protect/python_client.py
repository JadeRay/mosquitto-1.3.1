#!/usr/bin/env python
#import paho
import paho.mqtt.client as mqtt
import time
def on_connect(client, userdata, flags, rc):
	print ("Connected with result code "+ str(rc))
	
#	client.subscribe("$SYS/broker/load/protect/#")
#	client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
	print (msg.topic + " " + str(msg.payload))
	

client = mqtt.Client("python_client_test", True)
client.on_connect = on_connect
client.on_message = on_message

host = "127.0.0.1"

client.connect (host, 1883, 60)

topic = "/test/happy"
payload = "happy now?"
qos = 0
while True:
	client.publish(topic, payload, qos, False)
	print ("pub msg...")
	time.sleep(1)
