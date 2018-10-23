#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
# This is the Publisher
broker_ip = "192.168.31.241"
#client = mqtt.Client()
#client.connect(broker_ip)
def on_publish(client,userdata,result):             
    print("data published \n")
    pass
client= mqtt.Client()                           


client.connect("35.185.1.98",31500,60)


client.on_publish = on_publish                 
#client.subscribe("topic/test",2)
#time.sleep(1)

ret= client.publish("topic/test","Hello") 
time.sleep(2)

print(ret)

client.disconnect()
