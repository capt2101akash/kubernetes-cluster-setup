#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time

def on_publish(client,userdata,result):
    print("data published \n")
    pass

client= mqtt.Client()

client.on_publish = on_publish

client.connect("35.185.1.98",31500,60)


client.subscribe("topic/test", 2)
time.sleep(2)
try:
    while True:
        ret= client.publish("topic/test","Hello")
        time.sleep(4)
        print(ret)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()


