import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import json
import Adafruit_DHT

broker_address = "192.168.0.185"
pin = 2 #GPIO 2
sensor = Adafruit_DHT.DHT11

mqttc = mqtt.Client("P2")
mqttc.connect(broker_address, 1883, 60)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    #temperature = 20
    #humidity = 30
    data = {
        'temp':temperature,
        'humi':humidity
    }
    jsonString = json.dumps(data)

    print("Temp={0:0.01f}*C Humidity={1:0.01f}%".format(temperature, humidity))
    mqttc.publish("test", jsonString)
    time.sleep(3)

