import cv2 
import numpy as np
import serial
import random
import serial
import time
import matplotlib.pyplot
ser=serial.Serial("/dev/ttyUSB0",115200,timeout=0.05)



COLOR_MAP = {
    "white": (255, 255, 255),
    "green": (0, 255, 0),
    "red": (0, 0, 255),
    "blue" :(255, 0, 0)
}

alpha=1
beta=0.5
gamma=0

img=cv2.imread('./first1.jpeg')
tissue=cv2.resize(img,(800,800))
bg=cv2.resize(img,(800,800))


width=round(tissue.shape[0]/4)
height=round(tissue.shape[1]/4)

count=1
while count>0:
    count=count+1
    img=cv2.imread('./first1.jpeg')
    tissue=cv2.resize(img,(800,800))
    bg=cv2.resize(img,(800,800))
    word=cv2.resize(img,(800,800))
    x=[]
    start_x=0
    start_y=0
    end_x=width
    end_y=height
    temp=[]
    mask=tissue
    for i in range(16):
        data=ser.readline()
        data=data.decode() 
        if data != 'done\r\n' and data!='':
            if end_x>800:
                start_x=0
                end_x=width
                start_y=start_y+height
                end_y=end_y+height
            
        
            x.append([float(data)])
            if len(x)==4:
                temp.append(x)
                x=[]
            write=cv2.putText(word, str(data[:5]), (int(start_x+width/2), int(start_y+height/2)), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
            start_x=start_x+width
            end_x=end_x+width
    
        else:
            break

    #print(temp)
    if temp !=[]:
        temp.append([[30],[30],[45],[45]])
        ar=np.array(temp)

        #print(ar)
        cv2.normalize(ar,ar,0,255,cv2.NORM_MINMAX)
        ar=ar.tolist()
        #print(ar)
        ar=ar[:4]
        
        ar=np.array(ar)
        cv2.imwrite('2.jpg',ar)
        imjj=cv2.imread('2.jpg')
        imjj=cv2.resize(imjj,(800,800))
        heatmap = cv2.applyColorMap(imjj, cv2.COLORMAP_JET)
        mask=cv2.addWeighted(bg,alpha,heatmap,beta,gamma)
        cv2.namedWindow('temperature change diagram',0)
        cv2.resizeWindow('temperature change diagram',400,400)
        cv2.imshow('temperature change diagram',mask)
        cv2.namedWindow('temperature change text',0)
        cv2.resizeWindow('temperature change text',400,400)
        cv2.imshow('temperature change text',word)
        cv2.waitKey(1)
    if count %100==0:
        ser.close()
        ser.open()
    #print('next')
    #cv2.destroyAllWindows()
#print('out')
