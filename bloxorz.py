import pygame, math


screen_width = 1000
screen_height = 600
startX = 100
startY = 200
length = 25
width = 30
ang = 15

display = pygame.display.set_mode((screen_width,screen_height))

class Block:
    def __init__(self):
        self.x = 100
        self.y = 200
        self.width = 40
        self.height = 30

    def drawVertical(self):
        x,y,w,h = self.x,self.y,self.width,self.height
        b_w = 80

        pygame.draw.polygon(display,(255,0,0),[(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang+w,y-10+h-b_w),(x-10+w,y-10-b_w)])#Mat phai
        pygame.draw.polygon(display,(0,255,0),[(x-10+w,y-10),(x-10,y),(x-10,y-b_w),(x-10+w,y-10-b_w)]) #Mat sau
        pygame.draw.polygon(display,(0,0,255),[(x-10,y),(x+ang,y+h),(x+ang,y+h-b_w),(x-10,y-b_w)]) #Mat trai
        pygame.draw.polygon(display,(255,255,255),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h-b_w),(x+ang+w,y-10+h-b_w)])  #Mat truoc
        pygame.draw.line(display,(0,255,0),(x+ang+w,y-10+h),(x+ang+w,y-10+h-b_w)) #Cot truoc phai
        pygame.draw.line(display,(255,0,0),(x+ang,y+h),(x+ang,y+h-b_w)) #Cot truoc trai


    def drawHorizontalX(self):
        x,y,w,h = self.x,self.y,self.width,self.height
        b_w = 40
        deltax=40
        deltay=10
        pygame.draw.polygon(display,(255,0,0),[(x+deltax-10+w,y-deltay-10),(x+deltax+ang+w,y-deltay-10+h),(x+deltax+ang+w,y-deltay-10+h-b_w),(x+deltax-10+w,y-deltay-10-b_w)])#Mat phai
        pygame.draw.polygon(display,(0,255,0),[(x+deltax-10+w,y-deltay-10),(x-10,y),(x-10,y-b_w),(x+deltax-10+w,y-10-b_w-deltay)]) #Mat sau
        pygame.draw.polygon(display,(0,0,255),[(x-10,y),(x+ang,y+h),(x+ang,y+h-b_w),(x-10,y-b_w)]) #Mat trai
        pygame.draw.polygon(display,(255,255,255),[(x+deltax+ang+w,y-deltay-10+h),(x+ang,y+h),(x+ang,y+h-b_w),(x+deltax+ang+w,y-10+h-b_w-deltay)])  #Mat truoc
        pygame.draw.line(display,(0,255,0),(x+deltax+ang+w,y-deltay-10+h),(x+deltax+ang+w,y-deltay-10+h-b_w)) #Cot truoc phai
        pygame.draw.line(display,(255,0,0),(x+ang,y+h),(x+ang,y+h-b_w)) #Cot truoc trai

    def drawHorizontalY(self):
        x,y,w,h = self.x,self.y,self.width,self.height
        b_w = 40
        deltaX = 25
        deltaY = 30
        pygame.draw.polygon(display,(255,0,0),[(x-10+w,y-10),(x+ang+w+deltaX,y-10+h+deltaY),(x+ang+w+deltaX,y-10+h-b_w+deltaY),(x-10+w,y-10-b_w)])#Mat phai
        pygame.draw.polygon(display,(0,255,0),[(x-10+w,y-10),(x-10,y),(x-10,y-b_w),(x-10+w,y-10-b_w)]) #Mat sau
        pygame.draw.polygon(display,(0,0,255),[(x-10,y),(x+ang+deltaX,y+h+deltaY),(x+ang+deltaX,y+h-b_w+deltaY),(x-10,y-b_w)]) #Mat trai
        pygame.draw.polygon(display,(255,255,255),[(x+ang+w+deltaX,y-10+h+deltaY),(x+ang+deltaX,y+h+deltaY),(x+ang+deltaX,y+h-b_w+deltaY),(x+ang+w+deltaX,y-10+h-b_w+deltaY)])  #Mat truoc
        #pygame.draw.line(display,(0,255,0),(x+ang+w-deltaX,y-10+h-deltaY),(x+ang+w-deltaX,y-10+h-b_w-deltaY)) #Cot truoc phai
        pygame.draw.line(display,(255,0,0),(x+ang+deltaX,y+h+deltaY),(x+ang+deltaX,y+h-b_w+deltaY)) #Cot truoc trai

    def rotate_around(self,degrees,centre,point):
        x,y = point
        degrees = math.radians(degrees)
        pX,pY = centre
        rotX = pX + (math.cos(degrees)*(x-pX))-(math.sin(degrees)*(y-pY))
        rotY = pY + (math.sin(degrees)*(x-pX))-(math.cos(degrees)*(y-pY))
        return (int(rotX),int(rotY))

class Tile:
    def __init__(self,x=100,y=100):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 30

    def draw(self):
        x,y,w,h = self.x,self.y,self.width,self.height
        pygame.draw.polygon(display,(199,208,207),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)]) #Mat tren
        pygame.draw.polygon(display,(0,0,0),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)],1) #Vien mat tren
        pygame.draw.line(display,(45,56,65),(x-10,y),(x-10,y+10))
        pygame.draw.line(display,(45,56,65),(x+ang+w,y-10+h),(x+ang+w,y+h))
        pygame.draw.line(display,(45,56,65),(x+ang,y+h),(x+ang,y+h+10))

        pygame.draw.polygon(display,(45,56,65),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)]) # Mat trai
        pygame.draw.polygon(display,(0,0,0),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)],1)
        pygame.draw.polygon(display,(45,56,65),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h+10),(x+ang+w,y+h)]) # Mat truoc
        pygame.draw.polygon(display,(0,0,0),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h+10),(x+ang+w,y+h)],1)


def draw_level(level_data):
    x,y=startX,startY
    i=1
    for row in level_data:
        for tile_data in row:
            if(tile_data == 1):
                Tile(x,y).draw()
            x+=40
            y-=10
        x=startX+(i*length)
        y=startY+(i*width)
        i+=1
state=0
def handle_events():
    for e in pygame.event.get():
        if(e.type == pygame.KEYDOWN):
            if(e.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if(e.key == pygame.K_LEFT):
                bloxor.x-=40
                bloxor.y+=10
                print("LEFT")
            if(e.key == pygame.K_RIGHT):
                bloxor.x+=40
                bloxor.y-=10
                state=1
                print("RIGHT")
            if(e.key == pygame.K_UP):
                bloxor.x+=40
                bloxor.y-=10
                print("UP")
            if(e.key == pygame.K_DOWN):

                print("DOWN")
        if(e.type == pygame.QUIT):
            pygame.quit()
            quit()

bloxor = Block()
pygame.init()
pygame.display.set_caption("Bloxorz")
level_array = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,1,1,0,0,0,0,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,0,0,0],
               [0,0,0,1,1,1,1,1,1,1,1,1,0,0],
               [0,0,0,0,0,0,0,1,1,-1,1,1,0,0],
               [0,0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
def drawBlo(x,y,oriented):
    #clock.tick(30)
    display.fill((193,39,1)) #fill screen white
    bloxor.x=100+y*40+25*x
    bloxor.y=200-y*10+30*x
    draw_level(level_array)
    if oriented==0:
        bloxor.drawVertical()
    elif oriented==1:
        bloxor.drawHorizontalY()
    else:
        bloxor.drawHorizontalX()

    pygame.display.flip() #update screen
