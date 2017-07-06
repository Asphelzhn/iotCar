import thread
import threading
import RPi.GPIO as GPIO
import red
import time
import fire
import distance
import socket
from ip import get_ip

IN1 = 11
IN2 = 7
IN3 = 13
IN4 = 15

PWML = 40
PWMR = 38

S_HIGH = 25
S_LOW  = 15

fire_turn_L = 3.3
fire_turn_R = 3.5
bar_turn_L = 3.7
bar_turn_R = 5
ahead_time = 3.5

flag = threading.Event()
flag.set()

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(IN3,GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)
    GPIO.setup(PWML,GPIO.OUT)
    GPIO.setup(PWMR,GPIO.OUT)

def ahead():
    pL.ChangeDutyCycle(S_LOW)
    pR.ChangeDutyCycle(S_LOW)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)


def back():
    pL.ChangeDutyCycle(S_LOW)
    pR.ChangeDutyCycle(S_LOW)
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)

def left():
    pL.ChangeDutyCycle(S_HIGH)
    pR.ChangeDutyCycle(S_HIGH)
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)

def right():
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

def auto():
    while True:
        if(flag.isSet()==False):
            time.sleep(0.1)
            continue
        flame=fire.detectfire()
        dist = distance.distance()
        count_fire=0
    
        for i in range(len(flame)):
            if(flame[i]==1):
                count_fire+=1

        print '------------------------------------'
        print 'fire'+str(flame)
        print 'dist'+str(dist)
    	print '------------------------------------'

    	if(count_fire<4 and dist>10):
            ahead()
            print 'Go Ahead!'
    	elif(count_fire>=4):
            print 'Fire! Go right over here!'
            stop()
            time.sleep(1)
            right()
            time.sleep(fire_turn_R)
            time.sleep(1)
            ahead()
            time.sleep(ahead_time)
            stop()
            time.sleep(1)
            left()
            time.sleep(fire_turn_L)
            time.sleep(1)
            ahead()
            print 'Finished past fire!'
        elif(dist<=10):
            print 'Barrier! Go right over here!'
            stop()
            time.sleep(1)
            left()
            time.sleep(bar_turn_L)
            time.sleep(1)
            ahead()
            time.sleep(ahead_time)
            time.sleep(1)
            stop()
            time.sleep(1)
            right()
            time.sleep(bar_turn_R)
            time.sleep(1)
            ahead()
            print 'Finished past barrier'
	else:
            stop()
        time.sleep(0.11)

print (get_ip())
ip_port = (get_ip(),12345)
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
sk.bind(ip_port)
init()
pL=GPIO.PWM(PWML,20)
pR=GPIO.PWM(PWMR,20)
pL.start(S_LOW)
pR.start(S_LOW)

def manual():
    while True:
        data = sk.recv(1024)
        if(data=='ahead'):
            pL.ChangeDutyCycle(S_LOW)
            pR.ChangeDutyCycle(S_LOW)
            flag.clear()
            ahead()
        elif(data=='left'):
            pL.ChangeDutyCycle(S_HIGH)
            pR.ChangeDutyCycle(S_HIGH)
            flag.clear()
            left()
        elif(data=='right'):
            pL.ChangeDutyCycle(S_HIGH)
            pR.ChangeDutyCycle(S_HIGH)
            flag.clear()
            right()
        elif(data=='back'):
            pL.ChangeDutyCycle(S_LOW)
            pR.ChangeDutyCycle(S_LOW)
            back()
            flag.clear()
        else:
            flag.set()
            #auto()
        print (data)


thread.start_new_thread(manual,())
#thread.start_new_thread(auto,())
auto()

GPIO.cleanup()

