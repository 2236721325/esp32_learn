import bluetooth


bt = bluetooth.Bluetooth()
bt.set_advertisement("esp32")
bt.set_pin("1234")
bt.start()

while True:
    if bt.is_connected():
        print("已经连接")
        break
