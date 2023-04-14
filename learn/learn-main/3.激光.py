from machine import Pin, PWM
import machine
import time


pin18 = Pin(18, Pin.OUT)
while True:
    pin18.value(1)