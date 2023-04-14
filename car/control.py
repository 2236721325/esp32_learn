from machine import Pin
import time


p_right_up_1=Pin(13,Pin.OUT)
p_right_up_2=Pin(12,Pin.OUT)

p_left_up_1=Pin(15,Pin.OUT)
p_left_up_2=Pin(14,Pin.OUT)



p_right_down_1=Pin(17,Pin.OUT)

p_right_down_2=Pin(16,Pin.OUT)


p_left_down_1=Pin(18,Pin.OUT)

p_left_down_2=Pin(19,Pin.OUT)


def forward():
    p_left_up_1.value(1)
    p_left_up_2.value(0)
    p_left_down_1.value(1)
    p_left_down_2.value(0)
    p_right_down_1.value(1)
    p_right_down_2.value(0)
    p_right_up_1.value(1)
    p_right_up_2.value(0)

    
    
def stop():
    p_left_up_1.value(0)
    p_left_up_2.value(0)
    p_left_down_1.value(0)
    p_left_down_2.value(0)
    p_right_down_1.value(0)
    p_right_down_2.value(0)
    p_right_up_1.value(0)
    p_right_up_2.value(0)
    
def down():
    p_left_up_1.value(0)
    p_left_up_2.value(1)
    p_left_down_1.value(0)
    p_left_down_2.value(1)
    p_right_down_1.value(0)
    p_right_down_2.value(1)
    p_right_up_1.value(0)
    p_right_up_2.value(1)
    
    
    
def left():
    p_left_up_1.value(0)
    p_left_up_2.value(0)
    p_left_down_1.value(0)
    p_left_down_2.value(0)
    p_right_down_1.value(1)
    p_right_down_2.value(0)
    p_right_up_1.value(1)
    p_right_up_2.value(0)
    
def right():
    p_left_up_1.value(1)
    p_left_up_2.value(0)
    p_left_down_1.value(1)
    p_left_down_2.value(0)
    p_right_down_1.value(0)
    p_right_down_2.value(0)
    p_right_up_1.value(0)
    p_right_up_2.value(0)

# while True:
#     forward()
#     time.sleep(2)
#     stop()
#     time.sleep(2)
#     down()
#     time.sleep(2)
#     left()
#     time.sleep(2)
#     right()
#     time.sleep(2)
    
        







    


