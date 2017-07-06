#-*-coding:utf-8-*-


import RPi.GPIO as gpio  #第一行引用后，可以设置中文注释
import time

gpio.setwarnings(False)
def distance():
    gpio.setmode(gpio.BOARD)
    gpio.setup(12,gpio.OUT)
    gpio.setup(16,gpio.IN)
    gpio.output(12,True)  #发出触发信号保持10us以上（15us）
    time.sleep(0.000015)
    gpio.output(12,False)
    while not gpio.input(16):
        pass
    t1 = time.time()              #发现高电平时开时计时
    while gpio.input(16):
        pass
    t2 = time.time()              #高电平结束停止计时
    print((t2-t1)*34000/2)        #返回距离，单位为厘米
    gpio.cleanup()
distance()
