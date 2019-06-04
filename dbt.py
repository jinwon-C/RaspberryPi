import Adafruit_DHT as dht
import time

sensor = dht.DHT11
pin = 2

while True:
    humidity, temperature = dht.read_retry(sensor, pin)
    print("Temp={0:0.1f}*C Humi={1:0.1f}%".format(temperature, humidity))
    time.sleep(2)        
