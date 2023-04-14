from machine import Pin
import time


# 引脚配置
p13 = Pin(13, Pin.IN)
p2 = Pin(2,Pin.OUT)

while True:
    ret = p13.value()  # 读取传感器数据
    print(ret)
    
 
    time.sleep(0.1)
