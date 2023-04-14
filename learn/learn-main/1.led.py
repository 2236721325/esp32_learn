from machine import Pin, PWM
import machine
import time

# 亮灭效果
def test1():
    #GPIO2
    pin2 = Pin(2, Pin.OUT)
    while True:
        pin2.value(1)
        time.sleep(1)
        pin2.value(0)
        time.sleep(1)


def test2():
    led2=PWM(Pin(2))
    # 控制频率
    led2.freq(1000)
    # 控制占空比 来控制亮度
    led2.duty(50)
    
# 呼吸灯效果
def test3():
     led2=PWM(Pin(2))
     while True:
         for i in range(1024):
             led2.duty(i)
             time.sleep_ms(1)
         for i in range(1024):
             led2.duty(1023-i)
             time.sleep_ms(1)
         

test3()
    