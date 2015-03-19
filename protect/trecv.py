#!/usr/bin/env python
#coding=utf-8
import paho.mqtt.client as mqtt
import time
import redis

attr = {}
attrlist = ["rc", "rp", "rep", "rao"]

def check_protocol(payload):
    return False

def on_connect(client, userdata, flags, rc):
	print ("Connected with result code "+ str(rc))
	client.subscribe("/protect/rc/#")
	client.subscribe("/protect/rp/#")
	client.subscribe("/protect/rep/#")
	client.subscribe("/protect/rao/#")

def on_message(client, userdata, msg):
	print (msg.topic + " " + str(msg.payload))
	topics = msg.topic.split("/")
	topic_type = topics[-2]
	username = topics[-1]
	userexist = False
	if attr.has_key(username):
	    pass
	else:
	    attt[username] = [0, 0, 0, 0, 0] #rc,rp,rep,rao,uas
	for i in rage(4):
	    if topic_type == attrlist[i]:
		if i != 3:
		    freq = int(msg.payload)
		    attr[username][i] = attr[username][i] + freq
		else:
		    if check_protocol(msg.payload):
			pass
		    else:
			attr[username][i] += 1
		break


def main():	

    
    client = mqtt.Client("recv_client", True)
    client.username_pw_set("zhouyao", "123456")

    client.on_connect = on_connect
    client.on_message = on_message

    host = "127.0.0.1"

    client.connect (host, 1883, 60)

    last_update_time = int(time.time())
    interval = 5*60

    while True:
	now = int(time.time())
	if now - last_update_time > interval:
	    div_interval = now - last_update_time

	    for key in attr.keys():
		attr[key][-1] = cal_uas(attr[0:-1], div_interval)
		if attr[key][-1] > threshold:
		    db.add_tmp_bl(key)
		else:
		    pass
		attr[key] = [0]*5

	    last_update_time = now
	

		    

if __name__ == "__main__":
    main()

