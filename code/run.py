#-*-coding:utf-8-*-

import RPi.GPIO as GPIO
import time
import sys
import random



IN1 = 11
IN2 = 7 
IN3 = 13
IN4 = 15

PWML = 40
PWMR = 38


S_HIGH = 30 
S_LOW  = 15


 
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(IN3,GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)
    GPIO.setup(PWML,GPIO.OUT)
    GPIO.setup(PWMR,GPIO.OUT)
 
def qianjin():
    stop()
    pL.ChangeDutyCycle(S_LOW)
    pR.ChangeDutyCycle(S_LOW)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)

 
def houtui():
    stop()
    pL.ChangeDutyCycle(S_LOW)
    pR.ChangeDutyCycle(S_LOW)
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
 
def zuoxuan():
    stop()
    pL.ChangeDutyCycle(S_HIGH)
    pR.ChangeDutyCycle(S_HIGH)
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
 
def youxuan():
    stop()
    pL.ChangeDutyCycle(S_HIGH)
    pR.ChangeDutyCycle(S_HIGH)
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)

def stop():
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)

init()
pL=GPIO.PWM(PWML,20)
pR=GPIO.PWM(PWMR,20)
pL.start(S_LOW)
pR.start(S_LOW)



def distance():

    init()



    gpio.output(12,True) 

    time.sleep(0.000015)

    gpio.output(12,False)

    while not gpio.input(16):

        pass

    t1 = time.time()              #发现高电平时开时计时

    while gpio.input(16):

        pass

    t2 = time.time()              #高电平结束停止计时



    return (t2-t1)*34000/2        #返回距离，单位为厘米

    gpio.cleanup()

    return distance



def check_front():

    init()

    dist = distance()



    if dist < 15:

       print('close',dist)

       init()

       houtui(1)           #速度大快后退1S足够

       init()

       dist = distance()

       if dist < 15:

          print('too close',dist)

          init()

          zuoxuan(3)

          init()

          houtui(1)

          dist = distance()

          if dist<15:

             print('too too close',dist)

             tingzhi(2)



def autonomy():

    tf = 0.1

    x = random.randrange(0,5)



    if x==0:

       check_front()

       init()

       qianjin(0.2)      #前进的时间稍微长一些，效果好一点

       print '前进程序被执行。现在地距离是: %0.2f cm' %distance()

    elif x==1:

         check_front()

         init()

         zuoxuan(0.2)

         print '左旋程序被执行。现在地距离是: %0.2f cm' %distance()

    elif x==2:

         check_front()

         init()

         youxuan(tf)

         print '右旋程序被执行。现在地距离是: %0.2f cm' %distance()

    elif x==3:

         check_front()

         init()

         zuozhuan(tf)

         print '左转程序被执行。现在地距离是: %0.2f cm' %distance()

    elif x==4:

         check_front()

         init()

         stop(tf)

         print '右转程序被执行。现在地距离是: %0.2f cm' %distance()



try:

    while True:

          autonomy()

except KeyboardInterrupt:

    gpio.cleanup()
