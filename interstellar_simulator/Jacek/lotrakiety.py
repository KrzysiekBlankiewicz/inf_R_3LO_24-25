import pygame
import math
import random

#dane
file = open('danerakieta.txt', 'r').readlines()
    
xR = int(file[0])
yR = int(file[1])
vxR = int(file[2])
mR = int(file[3])
vRangle = int(file[4])
xP1 = int(file[5])
yP1 = int(file[6])
mP1 = int(file[7])
xP2 = int(file[8])
yP2 = int(file[9])
mP2 = int(file[10])
xP3 = int(file[11])
yP3 = int(file[12])
mP3 = int(file[13])
xP4 = int(file[14])
yP4 = int(file[15])
mP4 = int(file[16])
vyR = int(file[17])
aX = int(file[18])
aY = int(file[19])

sizeX =1000
sizeY = 1000

czas=5

color=(255,255,255)

line_color=(255,0,0)
 
pygame.init()
screen = pygame.display.set_mode([sizeX, sizeY])

#funkcje
class Rakieta:
    def __init__(self,xR,yR,vxR,vyR,mR,aX,aY):
        self.xR = xR
        self.yR = yR
        self.vxR = vxR
        self.vyR = vyR
        self.mR = mR
        self.aX = aX
        self.aY = aY
        
    def draw(self,screen,size):
        pygame.draw.circle(screen,(0,0,255),(self.xR,self.yR),size)

def gravity (mR , mP ,xR ,yR ,xP,yP):
    G=10
    r=max(distance(xR,yR,xP,yP),1)
    return G*(mR*mP)/(r**2)

class Planet:
    def __init__(self,xP,yP,mP) :
        self.xP = xP
        self.yP = yP
        self.mP = mP

    def draw(self,screen,size):
        pygame.draw.circle(screen,(150,0,200),(self.xP,self.yP),size)

    def drawF(self,screen):
        pygame.draw.line(screen,line_color, (rakieta.xR, rakieta.yR), (self.xP, self.yP))
        
def distance (xR,yR,xP,yP):
        return math.sqrt((xR - xP)**2 + (yR - yP)**2)


rakieta = Rakieta(xR, yR, vxR, vyR, mR , aX, aY)
listaP = [
    Planet(xP1, yP1, mP1),
    Planet(xP2, yP2, mP2),
    Planet(xP3, yP3, mP3),
    Planet(xP4, yP4, mP4)]

#dzialanie
running = True
 
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(color)

    for planet in listaP:
        planet.draw(screen, size=20)
        planet.drawF(screen)
    
    rakieta.draw(screen,10)

    Fx=0
    Fy=0
    for planet in  listaP:
        F = gravity(rakieta.mR, planet.mP, rakieta.xR, rakieta.yR, planet.xP, planet.yP)
        dX= planet.xP - rakieta.xR
        dY= planet.yP - rakieta.yR
        r = distance(rakieta.xR, rakieta.yR, planet.xP, planet.yP)
        Fx+=F*dX/100
        Fy+=F*dY/100
        pygame.draw.line(screen,(0,255,0), (rakieta.xR, rakieta.yR), ((rakieta.xR+dX/r*50), (rakieta.yR+dY/r*50)),3)
    
    rakieta.aX = Fx/mR
    rakieta.aY = Fy/mR
    
    rakieta.vxR += rakieta.aX
    rakieta.vyR += rakieta.aY

    rakieta.xR += rakieta.vxR / 100
    rakieta.yR += rakieta.vyR / 100
    
    if rakieta.xR < 0 or rakieta.xR > sizeX or rakieta.yR < 0 or rakieta.yR > sizeY:
        print("Rakieta wyleciałłła!!!")
        rakieta.xR=random.randint(0, sizeX)
        rakieta.yR=random.randint(0, sizeX)
        color=(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        
    pygame.display.flip() 
    pygame.time.wait(czas)

pygame.quit()
