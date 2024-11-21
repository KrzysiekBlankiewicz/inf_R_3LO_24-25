import pygame
import math
import random

sizeX =1000
sizeY = 1000
 
screen = pygame.display.set_mode([sizeX, sizeY])
pygame.init()
 
class Rocket:
    def __init__(self,xR,yR,vR,mR,angle):
        self.xR = xR
        self.yR = yR
        self.vR = vR
        self.mR = mR
        self.angle = angle
    def draw(self,screen,size):
        pygame.draw.circle(screen,(200,200,0),(self.xR,self.yR),size)
       
class Planet:
    def __init__(self,xP,yP,mP) :
        self.xP = xP
        self.yP = yP
        self.mP = mP
    def draw(self,screen,size):
        pygame.draw.circle(screen,(0,200,200),(self.xP,self.yP),size)
 
running = True
 
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rakietka = Rocket(500,500,100,5,5)
    
    P1 = Planet(200,900,100)
    P2 = Planet(100,100,150)
    P3 = Planet(900,500,100)
    P4 = Planet(500,250,100)



    P1.draw(screen,50)
    P2.draw(screen,100)
    P3.draw(screen,50)
    P4.draw(screen,10)

    rakietka.draw(screen,10)

    pygame.display.flip()

def distance (xR,yR,xP,yP):
    return ((xR-xP)**2 + (yR-yP)**2)**(1/2)

def gravity (mR , mP ,xR ,yR ,xP,yP):
    G=10
    r=distance(xR,yR,xP,yP)
    Fg=G*(mR*mP)/(r**2)
    return Fg
 
listaP=[P1,P2,P3,P4]
listaF=[]

for i in  listaP:
    F=gravity(mR , mP ,xR ,yR ,xP,yP)
    listaF.append(F)

pygame.quit()
