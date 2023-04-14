from machine import Pin,ADC
import time

# 模拟量
# sun_analog = ADC(Pin(15))
# sun_analog.atten(ADC.ATTN_11DB)  # 这里配置测量量程为3.3V


sun=Pin(15,Pin.IN)


while True:
    # print(sun_analog.read())
    print(sun.value())
    
    time.sleep(0.5)
