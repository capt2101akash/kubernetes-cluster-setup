from kafka import KafkaConsumer
import mysql.connector

def insert_into_db(msg):
  mydb = mysql.connector.connect( host="10.233.43.207", user="root", passwd="password", database="test" )
  mycursor = mydb.cursor()
  sql = "INSERT INTO test (name) VALUES ('" + msg + "')"
  mycursor.execute(sql)
  mydb.commit()


consumer = KafkaConsumer('topic1',
                         group_id='my-group',
                         bootstrap_servers=['35.185.1.98:32698'])
for message in consumer:
      print (message.value)

KafkaConsumer(consumer_timeout_ms=1000)
consumer = KafkaConsumer()
consumer.subscribe(pattern='^awesome.*')
