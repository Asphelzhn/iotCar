import RPi.GPIO as GPIO
import time
D1=22
D2=36
D3=18
D4=32
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(D1,GPIO.IN)
    GPIO.setup(D2,GPIO.IN)
    GPIO.setup(D3,GPIO.IN)
    GPIO.setup(D4,GPIO.IN)
def obstacle():
    init()
    while True:
        time.sleep(0.1)
        return (GPIO.input(D1),GPIO.input(D2),GPIO.input(D3),GPIO.input(D4))
    GPIO.cleanup()
