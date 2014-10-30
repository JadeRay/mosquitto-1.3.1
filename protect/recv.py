#!/usr/bin/env python
#import paho
import paho.mqtt.client as mqtt

average = [0, 0, 0, 2]
delta = [0.2, 0.2, 0.2, 5]

fobj = open("r_pub.csv", "w+")

def on_connect(client, userdata, flags, rc):
	print ("Connected with result code "+ str(rc))
	client.subscribe("$SYS/broker/load/protect/actscore")
	#client.subscribe("$SYS/broker/load/protect/#")
	

def on_message(client, userdata, msg):
	print (msg.topic + " " + str(msg.payload))
	recv = str(msg.payload)
	j = 0
	score_s = "" 
	for i in recv.split(','):
		val = float(i)
		if val < average[j] + delta[j]:
			score = 1
		else:
			score = (val - average[j])/delta[j]
		score_s += str(score)
		if j != 3:
			score_s += ","
		else:
			pass
		j = j + 1


	print ("score:" + score_s)	
	fobj.write(str(msg.payload) + "," + score_s + "\n")
	

client = mqtt.Client("recv_client", True)
client.on_connect = on_connect
client.on_message = on_message

host = "127.0.0.1"

client.connect (host, 1883, 60)

client.loop_forever()

fobj.close()
