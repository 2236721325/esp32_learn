
import dht
import machine
import time

d = dht.DHT11(machine.Pin(15))
while True:
    d.measure()
    print("{} °C".format(d.temperature()))
    print("{} RH".format(d.humidity()))
    time.sleep(0.5)
    print("-----------")
    