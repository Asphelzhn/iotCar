import RPi.GPIO as GPIO
import red
import time
import fire


IN1 = 11
IN2 = 7 
IN3 = 13
IN4 = 15

PWML = 40
PWMR = 38


S_HIGH = 30 
S_LOW  = 15


turn_time = 3.5

flag = 1 
 
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(IN3,GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)
    GPIO.setup(PWML,GPIO.OUT)
    GPIO.setup(PWMR,GPIO.OUT)
 
def ahead():
    stop()
    pL.ChangeDutyCycle(S_LOW)
    pR.ChangeDutyCycle(S_LOW)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)

 
def back():
    stop()
    pL.ChangeDutyCycle(S_LOW)
    pR.ChangeDutyCycle(S_LOW)
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
 
def left():
    stop()
    pL.ChangeDutyCycle(S_HIGH)
    pR.ChangeDutyCycle(S_HIGH)
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
 
def right():
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
while True:
    barrier=red.obstacle()
    flame=fire.detectfire()
    count_fire=0
    count_barrier=0
    for i in range(len(flame)):
        if(flame[i]==1):
            count_fire+=1
    for i in range(len(barrier)):
        if(barrier[i]==1):
            count_barrier+=1
            
    print 'barrier:'+str(barrier)
    print 'flame:'+str(flame)
    if(barrier[0]==0 and barrier[3]==0):
        flag = 0	
    elif(barrier[1]==0 and barrier[2]==0):
        flag = 1	
    elif(flag==1 and barrier[0]==1 and barrier[1]==1 and count_fire<4):
        ahead()
    elif(flag==1 and count_fire>=4):
        stop()
        time.sleep(0.1)
	right()
	time.sleep(turn_time)
	ahead()
	time.sleep(turn_time)
	left()
        time.sleep(turn_time)
        ahead()
    elif(flag==1 and (barrier[0]==0 or barrier[1]==0)):
        stop()
        time.sleep(0.1)
	right()
	time.sleep(turn_time)
	ahead()
	time.sleep(turn_time)
	left()
        time.sleep(turn_time)
        ahead()
    elif(flag==1 and (barrier[2]==0 or barrier[3]==0)):
        stop()
        time.sleep(0.1)
	right()
	time.sleep(4)
	ahead()
	time.sleep(4)
	left()
        time.sleep(4)
        ahead()
    else:
	stop()
GPIO.cleanup()
pL.stop()
pR.stop()

