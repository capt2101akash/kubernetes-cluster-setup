#!/usr/bin/env python3

import paho.mqtt.client as mqtt
# This is the Publisher
broker_ip = "192.168.31.241"
client = mqtt.Client()
#client.connect(broker_ip)
client.connect("192.168.31.241",1883,60)
if client.publish("topic/test", "Hello"):
    client.disconnect();
