from machine import Pin, PWM
import time
import machine

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('wyh', '7758mmMM')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


do_connect()

