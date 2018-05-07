import pygame, math
import time
x = 250
y = 25
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
screen_width = 1100
screen_height = 700
startX = 100
startY = 200
length = 25
width = 30
ang = 15

display = pygame.display.set_mode((screen_width,screen_height), pygame.NOFRAME)

class Block:
    def __init__(self):
        self.x = 100
        self.y = 200
        self.width = 40
        self.height = 30

    def drawVertical(self,oriented):
        x,y,w,h = self.x,self.y,self.width,self.height
        b_w = 0
        if(oriented==3):
            b_w=40
        else:
            b_w=80
        pygame.draw.polygon(display,(255,0,0),[(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang+w,y-10+h-b_w),(x-10+w,y-10-b_w)])#Mat phai
        pygame.draw.polygon(display,(0,255,0),[(x-10+w,y-10),(x-10,y),(x-10,y-b_w),(x-10+w,y-10-b_w)]) #Mat sau
        pygame.draw.polygon(display,(147,40,61),[(x-10,y),(x+ang,y+h),(x+ang,y+h-b_w),(x-10,y-b_w)]) #Mat trai
        pygame.draw.polygon(display,(220,59,90),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h-b_w),(x+ang+w,y-10+h-b_w)])  #Mat truoc
        pygame.draw.polygon(display,(255,78,123),[(x-10+w,y-10-b_w),(x+ang+w,y-10+h-b_w),(x+ang,y+h-b_w),(x-10,y-b_w)])#Mat tren

    def drawHorizontalX(self):
        x,y,w,h = self.x,self.y,self.width,self.height
        b_w = 40
        deltax=40
        deltay=10

        pygame.draw.polygon(display,(255,0,0),[(x+deltax-10+w,y-deltay-10),(x+deltax+ang+w,y-deltay-10+h),(x+deltax+ang+w,y-deltay-10+h-b_w),(x+deltax-10+w,y-deltay-10-b_w)])#Mat phai
        pygame.draw.polygon(display,(0,255,0),[(x+deltax-10+w,y-deltay-10),(x-10,y),(x-10,y-b_w),(x+deltax-10+w,y-10-b_w-deltay)]) #Mat sau
        pygame.draw.polygon(display,(147,40,61),[(x-10,y),(x+ang,y+h),(x+ang,y+h-b_w),(x-10,y-b_w)]) #Mat trai
        pygame.draw.polygon(display,(220,59,90),[(x+deltax+ang+w,y-deltay-10+h),(x+ang,y+h),(x+ang,y+h-b_w),(x+deltax+ang+w,y-10+h-b_w-deltay)])  #Mat truoc
        pygame.draw.polygon(display,(255,78,123),[(x+deltax-10+w,y-deltay-10-b_w),(x+deltax+ang+w,y-deltay-10+h-b_w),(x+ang,y+h-b_w),(x-10,y-b_w)]) #Mat tren
    def drawHorizontalY(self):
        x,y,w,h = self.x,self.y,self.width,self.height
        b_w = 40
        deltaX = 25
        deltaY = 30

        pygame.draw.polygon(display,(255,0,0),[(x-10+w,y-10),(x+ang+w+deltaX,y-10+h+deltaY),(x+ang+w+deltaX,y-10+h-b_w+deltaY),(x-10+w,y-10-b_w)])#Mat phai
        pygame.draw.polygon(display,(0,255,0),[(x-10+w,y-10),(x-10,y),(x-10,y-b_w),(x-10+w,y-10-b_w)]) #Mat sau
        pygame.draw.polygon(display,(147,40,61),[(x-10,y),(x+ang+deltaX,y+h+deltaY),(x+ang+deltaX,y+h-b_w+deltaY),(x-10,y-b_w)]) #Mat trai
        pygame.draw.polygon(display,(220,59,90),[(x+ang+w+deltaX,y-10+h+deltaY),(x+ang+deltaX,y+h+deltaY),(x+ang+deltaX,y+h-b_w+deltaY),(x+ang+w+deltaX,y-10+h-b_w+deltaY)])  #Mat truoc
        pygame.draw.polygon(display,(255,78,123),[(x-10+w,y-10-b_w),(x+ang+w+deltaX,y-10+h-b_w+deltaY),(x+ang+deltaX,y+h-b_w+deltaY),(x-10,y-b_w)])#Mat tren
class Tile:
    def __init__(self,x=100,y=100):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 30

    def draw(self,type,flag):
        x,y,w,h = self.x,self.y,self.width,self.height
        if type==1:
            pygame.draw.polygon(display,(249,252,255),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)]) #Mat tren
        elif type==2:
            pygame.draw.polygon(display,(0,255,0),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)]) #Mat tren
        elif type==3:
            pygame.draw.polygon(display,(0,0,255),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)]) #Mat tren
        elif type==4:
            pygame.draw.polygon(display,(255,0,0),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)]) #Mat tren
        elif type==5:#Gỗ
            pygame.draw.polygon(display,(200,200,0),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)]) #Mat tren
        elif type==-1:#Đích
            pygame.draw.polygon(display,(237,72,114),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)]) #Mat tren
        pygame.draw.polygon(display,(136,143,145),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)],1) #Vien mat tren
        pygame.draw.line(display,(136,143,145),(x+ang+w,y-10+h),(x+ang+w,y+h))
        pygame.draw.line(display,(136,143,145),(x+ang,y+h),(x+ang,y+h+10))

        if(not flag):
            pygame.draw.polygon(display,(185,185,191),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)]) # Mat trai
            pygame.draw.polygon(display,(136,143,145),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)],1)
        pygame.draw.polygon(display,(185,185,191),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h+10),(x+ang+w,y+h)]) # Mat truoc
        pygame.draw.polygon(display,(136,143,145),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h+10),(x+ang+w,y+h)],1)

def draw_level(level_data):
    x,y=startX,startY
    i=1
    for row in level_data:
        flag=0
        for tile_data in row:
            if(tile_data != 0):
                Tile(x,y).draw(tile_data,flag)
                flag=1
            else:
                flag=0
            x+=40
            y-=10
        x=startX+(i*length)
        y=startY+(i*width)
        i+=1
bloxor = Block()
pygame.init()
pygame.display.set_caption("Bloxorz")
level_array = []
def drawBlo(x1,y1,oriented=0,x2=0,y2=0):
    #clock.tick(30)
    display.fill((18,180,167)) #fill screen white
    bloxor.x=100+y1*40+25*x1
    bloxor.y=200-y1*10+30*x1
    draw_level(level_array)
    if oriented==0:
        bloxor.drawVertical(oriented)
    elif oriented==1:
        bloxor.drawHorizontalY()
    elif oriented==2:
        bloxor.drawHorizontalX()
    elif oriented==3:
        bloxor.drawVertical(oriented)
        bloxor2 = Block()
        bloxor2.x=100+y2*40+25*x2
        bloxor2.y=200-y2*10+30*x2
        bloxor2.drawVertical(oriented)
    pygame.display.flip() #update screen


