import pygame
import math

#dane
file = open('danerakieta.txt', 'r').readlines()
    
xR = int(file[0])
yR = int(file[1])
vR = int(file[2])
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

sizeX =1000
sizeY = 1000

czas=5

line_color=(255,0,0)
 
pygame.init()
screen = pygame.display.set_mode([sizeX, sizeY])

#funkcje
class Rakieta:
    def __init__(self,xR,yR,vR,mR,aR):
        self.xR = xR
        self.yR = yR
        self.vR = vR
        self.mR = mR
        self.aR = aR
        
    def draw(self,screen,size):
        pygame.draw.circle(screen,(0,0,255),(self.xR,self.yR),size)

def gravity (mR , mP ,xR ,yR ,xP,yP):
    G=10
    r=distance(xR,yR,xP,yP)
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


rakieta = Rakieta(xR, yR, vR, mR, vRangle)
listaP = [
    Planet(xP1, yP1, mP1),
    Planet(xP2, yP2, mP2),
    Planet(xP3, yP3, mP3),
    Planet(xP4, yP4, mP4)]

running = True
 
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))

    for planet in listaP:
        planet.draw(screen, size=100)
        planet.drawF(screen)

    rakieta.draw(screen,10)

    listaF=[]
    xS=rakieta.xR
    yS=rakieta.yR
    for planet in  listaP:
        F = gravity(rakieta.mR, planet.mP, rakieta.xR, rakieta.yR, planet.xP, planet.yP)
        dX=(planet.xP-rakieta.xR)*F/100
        dY=(planet.yP-rakieta.yR)*F/100
        pygame.draw.line(screen,(0,255,0), (rakieta.xR, rakieta.yR), ((rakieta.xR+dX), (rakieta.yR+dY)),3)
        xS+=0.001*dX
        yS+=0.001*dY
        # de facto xS, yS to są składowe siły wypadkowej podzielone przez 1000
        listaF.append(F)

    #rakieta.xR=xS
    #rakieta.yR=yS

    # jak policzyć Fwyp ze składowych? (xS, yS)
    Fwyp=distance(rakieta.xR,rakieta.yR,xS,yS)
    a=Fwyp/mR
    # aX = ? , aY = ?
    rakieta.vR+=a

    print(rakieta.vR)

    pygame.draw.line(screen,(255,255,255), (rakieta.xR, rakieta.yR), (xS,yS) ,5)

    pygame.display.flip() 
    pygame.time.wait(czas)

pygame.quit()
