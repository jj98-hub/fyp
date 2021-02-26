import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)   
GPIO.setmode(GPIO.BCM) 
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.output(16,True) 

while True:
    time.sleep(0.001)
    GPIO.output(20,False) 
    time.sleep(0.001)
    GPIO.output(20,True) 
