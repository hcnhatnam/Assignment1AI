import pygame, math
from pygame import gfxdraw

pygame.init()
screen_width = 700
screen_height = 400
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

        b_l = (x+ang,y+h)
        t_l = (x+ang,y+h-b_w)
        b_r = (x+ang+w,y-10+h)
        t_r = (x+ang+w,y-10+h-b_w)
        t_l_r = self.rotate_around(90,b_l,t_l)
        pygame.draw.circle(display,(255,255,255),t_l_r,10)

    def drawHorizontal(self):
        x,y,w,h = self.x,self.y,self.width,self.height
        b_w = 80
        pygame.draw.polygon(display,(255,0,0),[(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang+w,y-10+h-b_w),(x-10+w,y-10-b_w)])#Mat phai
        pygame.draw.polygon(display,(0,255,0),[(x-10+w,y-10),(x-10,y),(x-10,y-b_w),(x-10+w,y-10-b_w)]) #Mat sau
        pygame.draw.polygon(display,(0,0,255),[(x-10,y),(x+ang,y+h),(x+ang,y+h-b_w),(x-10,y-b_w)]) #Mat trai
        pygame.draw.polygon(display,(255,255,255),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h-b_w),(x+ang+w,y-10+h-b_w)])  #Mat truoc
        pygame.draw.line(display,(0,255,0),(x+ang+w,y-10+h),(x+ang+w,y-10+h-b_w)) #Cot truoc phai
        pygame.draw.line(display,(255,0,0),(x+ang,y+h),(x+ang,y+h-b_w)) #Cot truoc trai
        b_l = (x+ang,y+h)
        t_l = (x+ang,y+h-b_w)
        b_r = (x+ang+w,y-10+h)
        t_r = (x+ang+w,y-10+h-b_w)
        t_l_r = self.rotate_around(90,b_l,t_l)
        pygame.draw.circle(display,(255,255,255),t_l_r,10)

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
                print("RIGHT")
            if(e.key == pygame.K_UP):
                print("UP")
            if(e.key == pygame.K_DOWN):
                print("DOWN")
        if(e.type == pygame.QUIT):
            pygame.quit()
            quit()

bloxor = Block()
def main():

    pygame.display.set_caption("Bloxorz")
    #clock = pygame.time.Clock()

    #bloxor.x = 165
    #bloxor.y = 220

    #level_array = [[1]]

    level_array = [
        [1,1,1,0,0,0,0,0,0,0],
        [1,1,1,1,1,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,1,1,0,1,1],
        [0,0,0,0,0,0,1,1,1,0],
    ]
    while(True):
        #clock.tick(30)
        handle_events()
        display.fill((193,39,1)) #fill screen white

        draw_level(level_array)
        bloxor.drawVertical()

        pygame.display.flip() #update screen


if __name__ == "__main__":
    main()