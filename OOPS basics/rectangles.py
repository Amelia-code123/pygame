import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))

colour1=(23,55,211)
colour2=(54,122,65)
colour3=(98,67,111)
colour4=(67,90,2)
colour5=(46,86,243)

#filling the screen
screen.fill(colour1)
pygame.display.update()

#class for the rectangles
class rectangle():
    def __init__(self,colour,size):
        self.surface=screen
        self.colour=colour
        self.size=size
    
    #function for drawing rectangles
    def make(self):
        self.rect1=pygame.draw.rect(self.surface, self.colour, self.size)

#object creation
r1=rectangle(colour2,(100,100,100,100))
r2=rectangle(colour3,(400,100,100,100))
r3=rectangle(colour5,(100,400,400,100))

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    r1.make()
    r2.make()
    r3.make()
    pygame.display.update()

pygame.quit()