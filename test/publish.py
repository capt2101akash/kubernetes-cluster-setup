#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
# This is the Publisher
broker_ip = "192.168.31.241"
client = mqtt.Client()
#client.connect(broker_ip)
def on_publish(client,userdata,result):             
    print("data published \n")
    pass
client= mqtt.Client("testMqtt")                           

client.on_publish = on_publish                 

client.connect("35.196.15.47",31092,60)


client.subscribe("topic/test",2)
time.sleep(1)

ret= client.publish("topic/test","Hello") 
#time.sleep(2)

print(ret)

client.disconnect()
