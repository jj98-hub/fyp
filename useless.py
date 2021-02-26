import pygame
import time
import cv2
import RPi.GPIO as GPIO
# for motor setup
motor=26
dir1=19
motor2=20
dir2=16
GPIO.setwarnings(False)   
GPIO.setmode(GPIO.BCM) 
GPIO.setup(dir1,GPIO.OUT)
GPIO.setup(motor,GPIO.OUT)
GPIO.output(dir1,False)
GPIO.setup(dir2,GPIO.OUT)
GPIO.setup(motor2,GPIO.OUT)
GPIO.output(dir2,True )



while True:
    GPIO.output(motor2,False)
    time.sleep(0.0001)
    GPIO.output(motor2,True)
    time.sleep(0.0001)
    
