from machine import Pin, PWM
import machine
import time


pin18 = Pin(15, Pin.OUT)
while True:
    for i in range(10):
        pin18.value(1)
        time.sleep(0.2)
        pin18.value(0)
        time.sleep(0.2)