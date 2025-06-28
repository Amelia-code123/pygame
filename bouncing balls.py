import pgzrun,random

TITLE="bouncing ball game"
WIDTH=700
HEIGHT=600

red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)
colour=(red,green,blue)
gravity=2000.0

#class for ball
class ball():
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.vx=200
        self.vy=0
        self.size=size
    
    def draw(self):
        red=random.randint(0,255)
        green=random.randint(0,255)
        blue=random.randint(0,255)
        colour=(red,green,blue)
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.size,colour)

#object creation
ball1=ball(100,100,60)
ball2=ball(400,400,80)
all=[ball1,ball2]

def draw():
    for i in all:
        i.draw()

def update(ti):
    pass
    global all
    for i in all:
        uy=i.vy
        i.vy+=gravity*ti
        i.y+=(uy+i.vy)*0.5*ti
        #detecting and handling bounce
        if i.y>600:
            i.y=600
            i.vy=-i.vy*0.9
        i.x+=i.vx*ti
        if i.x<50 or i.x>650:
            i.vx=-i.vx

def on_key_down(key):
    if key==keys.SPACE:
        ball1.vy=-300
        ball2.vy=-250

pgzrun.go()
