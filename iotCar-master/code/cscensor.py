#-*-coding:utf-8-*-


import RPi.GPIO as gpio  #第一行引用后，可以设置中文注释

import time



gpio.setwarnings(False)   #去掉一些不必要的警告

zuoqian = 7               #7脚为控制左侧轮前进，11脚控制左侧轮子后退

zuohou = 11

youqian = 15              #15脚为控制右侧轮前进，13脚控制右侧轮子后退

youhou = 13



def init():

    gpio.setmode(gpio.BOARD) #GPIO调用BOARD编号方式

    gpio.setup(11,gpio.OUT)

    gpio.setup(7,gpio.OUT)

    gpio.setup(13,gpio.OUT)

    gpio.setup(15,gpio.OUT)



def qianjin(timerun):     #左右都往前，为前进

    init()                #初始化

    gpio.output(11,True)   #左侧轮子前进

    gpio.output(7,False)

    gpio.output(15,True)  #右侧轮子前进

    gpio.output(13,False)

    time.sleep(timerun)

    gpio.cleanup()         #演示timerum秒转动停止转动



def houtui(timerun):       #左右都往后，为前后

    init()               

    gpio.output(11,False)   #左侧轮子后退

    gpio.output(7,True)

    gpio.output(15,False)  #右侧轮子后退

    gpio.output(13,True)

    time.sleep(timerun)

    gpio.cleanup()         



def zuozhuan(timerun):     #左轮不动，右轮前进，为左转

    init()               

    gpio.output(11,False)   #左侧轮子不动

    gpio.output(7,False)

    gpio.output(15,True)   #右侧轮子前进
    gpio.output(13,False)

    time.sleep(timerun)

    gpio.cleanup()         #演示timerum秒转动停止转动



def youzhuan(timerun):     #左轮前进，右轮不动，为右转

    init()               

    gpio.output(11,True)    #左侧轮子前进

    gpio.output(7,False)

    gpio.output(15,False)  #右侧轮子不动

    gpio.output(13,False)

    time.sleep(timerun)

    gpio.cleanup()       



def zuoxuan(timerun):      #左轮后退，右轮前进，为左旋转

    init()               

    gpio.output(11,False)   #左侧轮子后退

    gpio.output(7,True)

    gpio.output(15,True)   #右侧轮子前进

    gpio.output(13,False)

    time.sleep(timerun)

    gpio.cleanup()         



def youxuan(timerun):      #左轮前进，右轮后退，为右旋转

    init()               

    gpio.output(11,True)    #左侧轮子前进

    gpio.output(7,False)

    gpio.output(15,False)  #右侧轮子后退

    gpio.output(13,True)

    time.sleep(timerun)

    gpio.cleanup()         



qianjin(1)                 #以下是各种联动测试1S，要测试哪项就把哪项之前的#去掉

#houtui(1)

#zuozhuan(1)

#youzhuan(1)

#zuoxuan(1)

#youxuan(1)

#这是终止行，以下返回正文
