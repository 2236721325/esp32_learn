from machine import Pin
import time


# 引脚配置
p15 = Pin(15, Pin.IN)

while True:
    ret = p15.value()  # 读取传感器数据
    print(ret)
    
 
    time.sleep(0.1)