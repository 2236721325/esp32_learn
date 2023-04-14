from machine import Pin, ADC
import time


# 模拟量
sound_analog = ADC(Pin(33))
sound_analog.atten(ADC.ATTN_11DB)  # 这里配置测量量程为3.3V


def sound_func(*argc):
    # print(argc)
    print("HasSound...")


# 数字量
p15 = Pin(15, Pin.IN)
p15.irq(trigger=Pin.IRQ_RISING, handler=sound_func)

# 循环检测
while True:
    sound_value = sound_analog.read()  # 0-4095
    print(sound_value)
