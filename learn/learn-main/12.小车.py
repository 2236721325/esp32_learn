from machine import Pin, PWM
import time
p12=Pin(12,Pin.OUT)
p13=Pin(13,Pin.OUT)

p14=Pin(14,Pin.OUT)
p15=Pin(15,Pin.OUT)
p16=Pin(16,Pin.OUT)
p17=Pin(17,Pin.OUT)

p18=Pin(18,Pin.OUT)
p19=Pin(19,Pin.OUT)



p2=Pin(2,Pin.OUT)


while True:
    p12.value(1)
    p13.value(0)
    p2.value(1)
    time.sleep(2)
    
    p12.value(0)
    p13.value(1)    
    time.sleep(2)
    
    
    p14.value(1)
    p15.value(0)
    p2.value(1)
    time.sleep(2)
    
    p14.value(0)
    p15.value(1)    
    time.sleep(2)
    
    
    
    
    p16.value(1)
    p17.value(0)
    time.sleep(2)
    
    p16.value(0)
    p17.value(1)    
    time.sleep(2)
    
    
    p18.value(1)
    p19.value(0)
    time.sleep(2)
    
    p18.value(0)
    p19.value(1)    
    time.sleep(2)


    


