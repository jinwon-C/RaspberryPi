import paho.mqtt.client as mqtt
import time
from datetime import datetime

mqtt = mqtt.Client()
mqtt.connect("192.168.0.157", 1883)

while True:
    now = datetime.now()
    mqtt.publish("topic", "Hello "+str(now))
    time.sleep(2)
    
