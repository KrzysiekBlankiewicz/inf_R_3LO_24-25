import pygame
import math
import random
sizeX =1000
sizeY = 1000

screen = pygame.display.set_mode([sizeX, sizeY])
pygame.init()

class Rocket:
    def __init__(self,rocketx,rockety,velocity,mass,angle):
        self.rocketx = rocketx
        self.rockety = rockety
        self.velocity =velocity
        self.mass = mass
        self.angle = angle
    def draw(self,screen,size):
        pygame.draw.circle(screen,(200,0,0),(self.rocketx,self.rockety),size)
        
class Planet:
    def __init__(self,planetx,planety,mass) :
        self.planetx = planetx
        self.planety = planety
        self.mass = mass
    def draw(self,screen,size):
        pygame.draw.circle(screen,(200,0,0),(self.planetx,self.planety),size)

def distance(x1,y1,x2,y2):
    return math.sqrt((x1+y1)**2,(x2+y2)**2)

def gravity(m1,m2,x1,y1,x2,y2):
    g =  6.67*10**(-11)
    r = distance(x1,y1,x2,y2)
    fg = g*m1*m2/r**2
    return fg


running = True

while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    rakietka = Rocket(500,100,100,5,5)
    planetka = Planet(69,811,100)
    planetka.draw(screen,50)
    planetka = Planet(500,400,100)
    planetka.draw(screen,50)
    planetka = Planet(100,30,100)
    planetka.draw(screen,50)

    rakietka.draw(screen,10)
    pygame.display.flip()

pygame.quit()
