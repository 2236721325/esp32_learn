from machine import ADC,Pin,PWM
import time


led2=PWM(Pin(2))


while True:
    for i in range(1024):
        led2.duty(i)
        time.sleep_ms(1)
    for i in range(1024):
        led2.duty(1023-i)
        time.sleep_ms(1)