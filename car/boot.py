import control
import time
import m_bluetooth


    
    
    
if __name__ == "__main__":
    ble = m_bluetooth.ESP32_BLE("ESP32_Car")
    while True:
        if ble.msg == 'forward':
            print(ble.msg)
            control.forward()
        elif ble.msg=='down':
            print(ble.msg)
            control.down()
        elif ble.msg=='stop':
            print(ble.msg)
            control.stop()
        elif ble.msg=='left':
            print(ble.msg)
            control.left()
        elif ble.msg=='right':
            print(ble.msg)
            control.right()

        ble.msg = ""
        time.sleep_ms(100)