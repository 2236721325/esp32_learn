from machine import Pin, PWM
import machine
import time


pin15 = Pin(15, Pin.OUT)
while True:
    # for i in range(10):
    #     pin15.value(1)
    #     time.sleep(0.2)
    #     pin15.value(0)
    #     time.sleep(0.2)
    
    
    pin15.off()
    
    time.sleep(1)
    
    pin15.on()
    
    time.sleep(1)