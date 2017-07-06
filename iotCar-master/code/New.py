import socket
import RPi.GPIO as GPIO
import time
from stop import get_ip

IN1 = 11
IN2 = 7
IN3 = 13
IN4 = 15

PWML = 40
PWMR = 38


S_HIGH = 35
S_LOW  = 15 
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(IN3,GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)
    GPIO.setup(PWML,GPIO.OUT)
    GPIO.setup(PWMR,GPIO.OUT)
 
def ahead():
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
 
def back():
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
 
def left():
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
 
def right():
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)

def stop():
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)

print (get_ip())

ip_port = (get_ip(),12345)
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
sk.bind(ip_port)
init()
pL=GPIO.PWM(PWML,20)
pR=GPIO.PWM(PWMR,20)
pL.start(S_LOW)
pR.start(S_LOW)
while True:
    data = sk.recv(1024)
    if(data=='ahead'):
        pL.ChangeDutyCycle(S_LOW)
        pR.ChangeDutyCycle(S_LOW)
        ahead()
    elif(data=='left'):
        pL.ChangeDutyCycle(S_HIGH)
        pR.ChangeDutyCycle(S_HIGH)
	left()
    elif(data=='right'):
        pL.ChangeDutyCycle(S_HIGH)
        pR.ChangeDutyCycle(S_HIGH)
        right()
    elif(data=='back'):
        pL.ChangeDutyCycle(S_LOW)
        pR.ChangeDutyCycle(S_LOW)
        back()
    else:
        stop()
    print (data)
    
GPIO.cleanup()
pL.stop()
pR.stop()
sk.close()
