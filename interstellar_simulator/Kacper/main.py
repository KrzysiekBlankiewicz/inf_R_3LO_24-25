import pygame
import math
import random
from rocket import Rocket
from planet import Planet
sizeX =1000
sizeY = 1000

planet_number = 4
planet_size = 30
planet_list=[]

screen = pygame.display.set_mode([sizeX, sizeY])
pygame.init()

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-y1)**2 + (x2-y2)**2)

def gravity(m1,m2,x1,y1,x2,y2):
    g =  6.67*10**(-11)
    r = distance(x1,y1,x2,y2)
    return g*m1*m2/r**2




for x in range(planet_number):
    planet = Planet(random.randint(1,1000),random.randint(1,1000),10)
    planet_list.append(planet)

def vector(m1,m2,x1,y1,x2,y2):
    fx = (x2-x1)*gravity(m1,m2,x1,y1,x2,y2)
    fy = (y2-y1)*gravity(m1,m2,x1,y1,x2,y2)
    return fx,fy

running = True

while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    rakieta = Rocket(500,500,100,100,100)
    rakieta.draw(screen,100)
    for x in planet_list:
        x.draw(screen,planet_size)
        print(gravity(rakieta.mass,x.mass,rakieta.rocketx,rakieta.rockety,x.planetx,x.planety))
        pygame.draw.line(screen,(0,0,200),(rakieta.rocketx,rakieta.rockety),[vector(rakieta.mass,x.mass,rakieta.rocketx,rakieta.rockety,x.planetx,x.planety)[0],vector(rakieta.mass,x.mass,rakieta.rocketx,rakieta.rockety,x.planetx,x.planety)[1]])
    pygame.display.flip()

pygame.quit()
print("HELLLO WORLD")
