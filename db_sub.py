import paho.mqtt.client as mqtt
import mysql.connector
import json
from mysql.connector import errorcode

db = mysql.connector.connect(
        host = "localhost",
        user="root",
        passwd="1234",
        db="sensorDB"
)

cur = db.cursor()
broker_address = "192.168.0.185"

def on_message(client, userdata, msg):
    data = str(msg.payload.decode("utf-8"))
    dict = json.loads(data)
    print("Received message = {}",data)

    cur.execute("insert into sensorTable values(now(), {}, {})".format(dict['temp'], dict['humi']))
    db.commit()
    cur.execute("select * from sensorTable")

    rows = cur.fetchall()
    for row in rows:
        print(rows)

client = mqtt.Client("P1")
client.on_message = on_message

print("connection to broker.")
client.connect(broker_address, 1883, 60)
client.subscribe("test")
client.loop_forever()



