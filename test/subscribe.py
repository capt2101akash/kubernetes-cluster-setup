import paho.mqtt.client as mqtt
from kafka import KafkaProducer
from kafka.errors import KafkaError
import time

def kafka_publish(msg):
  producer = KafkaProducer(bootstrap_servers=['10.233.43.121:9092'])
# Asynchronous by default
  future = producer.send('topic1', str(msg))
# Block for 'synchronous' sends
  try:
    record_metadata = future.get(timeout=8)
  except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass
# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  client.subscribe("topic/test", 2)
  print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
  if msg.payload:
    print(msg.payload.decode())
    kafka_publish(msg.payload.decode())

    
client = mqtt.Client()

client.connect("192.168.31.241",1883,60)
client.loop_start()
client.on_connect = on_connect
client.on_message = on_message
try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop() 
