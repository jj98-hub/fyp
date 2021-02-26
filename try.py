import pygame
import time
import cv2
import serial

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
            #ser=serial.Serial('com7',9600,timeout=10)
            for i in pos:
                x_ard.append(i[0])
                y_ard.append(i[1])
                da='x='+str(i[0])+','+'y='+str(i[1])+'.'
                da=str.encode(da)
            print(len(x_ard))
            xfin=[]
            yfin=[]
            xtime=[]
            ytime=[]
            for j in range (len(x_ard)):
                xdistance=x_ard[j]-x_pos
                ydistance=y_ard[j]-y_pos
                xfin.append(xdistance*10)
                yfin.append(ydistance*10)
                x_pos=x_ard[j]
                y_pos=y_ard[j]
                if abs(xdistance)>abs(ydistance) and ydistance!=0:
                    xtime.append(1);
                    ytime.append(abs(xdistance/ydistance))
                elif abs(xdistance)<abs(ydistance) and xdistance!=0:
                    ytime.append(1)
                    xtime.append(abs(ydistance/xdistance))
                elif xdistance==0 or  ydistance==0:
                    xtime.append(1)
                    ytime.append(1)


            print(xfin)
            print(yfin)
            print(xtime)
            print(ytime)
            pos=[]
            x_ard=[]
            y_ard=[]
            #pygame.quit()
        else:
            continue

pygame.quit()
