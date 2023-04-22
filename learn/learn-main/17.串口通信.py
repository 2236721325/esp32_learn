# code: gb2312               # 在串口屏中使用的字库的编码是gb2312
from machine import UART     # 导入串口模块
import time                  # 导入时间模块

uart = UART(2, 115200)       # 初始化串口2，并设置波特率为115200

uart.write(b"n0.val=700")    # 以二进制形式发送修改文本
time.sleep(2)                # 休息两秒，此行和上面那个导入时间模块的代码删了也行
                             # 加上是为了在回显中能让修改式和结束符能分行
uart.write(b"\xff\xff\xff")  # 发送结束符

uart.write(b"n0.val=600")
time.sleep(2) 
uart.write(b"\xff\xff\xff")

print(1)                     # 打印个1以表结束