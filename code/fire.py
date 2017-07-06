import RPi.GPIO as GPIO
import time
D1=29
D2=31
D3=33
D4=35
D5=37
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(D1,GPIO.IN)
    GPIO.setup(D2,GPIO.IN)
    GPIO.setup(D3,GPIO.IN)
    GPIO.setup(D4,GPIO.IN)
    GPIO.setup(D5,GPIO.IN)
def detectfire():
    init()
    while True:
        time.sleep(0.1)
        return [GPIO.input(D1),GPIO.input(D2),GPIO.input(D3),GPIO.input(D4),GPIO.input(D5)]
    GPIO.cleanup()
detectfire()
