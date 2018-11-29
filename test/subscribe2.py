import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
  client.subscribe("topic/test", 2)
  print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
  if msg.payload:
    print(msg.payload.decode())
    #kafka_publish(msg.payload.decode())


client = mqtt.Client()

client.connect("35.196.230.81",30797,60)
client.loop_start()
client.on_connect = on_connect
client.on_message = on_message
try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    #client.loop_stop()

