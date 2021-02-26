import cv2 
import numpy as np
import serial
import random
import serial
import time
import matplotlib.pyplot
ser=serial.Serial("/dev/ttyUSB0",115200,timeout=0.05)
temp=[]
x=[]
while True:
    times=time.time()
    for i in range(16):
        data=ser.readline()
        data=data.decode()
        if data != 'done\r\n' and data!='':
            temp.append([float(data)])
        else:
            break
    if temp != []:
        print(temp)
        print('done')
        print(time.time()-times)
    temp=[]

    
