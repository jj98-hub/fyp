import pygame
import time
import cv2
import RPi.GPIO as GPIO
import numpy
import matplotlib.pyplot
import multiprocessing as mp
cap = cv2.VideoCapture(0)
start=1
def for_cam(cap,start):
    while start:
        # for motor setup
        
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        cv2.waitKey(1)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyWindow("capture")

#
def for_walk(cap,start):
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
    GPIO.output(dir2,False) 
    #end of motor setup
    img=cv2.imread('./first1.jpeg')
    bg=cv2.resize(img,(500,500))
    cv2.imwrite('222.jpg',bg)
    pygame.init()
    win=pygame.display.set_mode((500,500))
    pygame.display.set_caption('laser shot path')
    x=50
    y=50
    width=40
    height=60
    vel=50
    bg=pygame.image.load('222.jpg')
    run=True
    flag=False
    x=100
    y=100
    r=5
    pos=[]
    x_ard=[]
    y_ard=[]
    x_pos=0
    y_pos=0
    win.blit(bg,(0,0))
    pygame.display.update()
    while run:
        pygame.time.delay(1)#milisecond
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                flag=True
                x,y=event.pos
                pygame.draw.circle(win,(255,0,0),(x,y),r)
                pygame.display.update()
                pos.append(event.pos)

            elif event.type==pygame.MOUSEBUTTONUP:
                flag=False
            elif event.type==pygame.MOUSEMOTION and flag:
                x,y=event.pos
                pygame.draw.circle(win,(255,0,0),(x,y),r)
                pygame.display.update()
                pos.append(event.pos)
        if keys[pygame.K_SPACE]:
            win.blit(bg,(0,0))
            pygame.display.update()
            if pos !=[]:   
                for i in pos:
                    x_ard.append(i[0])
                    y_ard.append(i[1])
                for i in  range (len(x_ard)):
                    xrange=x_ard[i]-x_pos
                    if xrange>0:
                        GPIO.output(dir1,False)
                    else:
                        GPIO.output(dir1,True)
                    yrange=y_ard[i]-y_pos
                    if yrange>0:
                        GPIO.output(dir2,False)
                    else:
                        GPIO.output(dir2,True)
                    if xrange!=0:
                        for j in range (abs(xrange)*10):
                            GPIO.output(motor,False)
                            time.sleep(0.001)
                            GPIO.output(motor,True)
                            time.sleep(0.001)
                    if yrange!=0:
                        for k in range (abs(yrange)*10):
                            GPIO.output(motor2,False)
                            time.sleep(0.001)
                            GPIO.output(motor2,True)
                            time.sleep(0.001)
                    if i==0:
                        time.sleep(2)
                    x_pos=x_ard[i]
                    y_pos=y_ard[i]

                time.sleep(2)
                GPIO.output(dir1,True)
                GPIO.output(dir2,True)
                for h in range(x_pos*10):
                            GPIO.output(motor,False)
                            time.sleep(0.0001)
                            GPIO.output(motor,True)
                            time.sleep(0.0001)
                for k in range(y_pos*10):
                            GPIO.output(motor2,False)
                            time.sleep(0.0001)
                            GPIO.output(motor2,True)
                            time.sleep(0.0001)
                #after everything done then do below
                print('draw again')
                pos=[]
                x_ard=[]
                y_ard=[]
                break
            else:
                continue


    start=0




if __name__=='__main__':
    p1 = mp.Process(target=for_walk,args=(cap,start,))
    p2 = mp.Process(target=for_cam,args=(cap,start,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
