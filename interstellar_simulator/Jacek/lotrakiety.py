import pygame
import math

file = open('rakietadane.txt').readlines()
file = [int(line.strip()) for line in file]
    
xR = file[0]
yR = file[1]
vR = file[2]
mR = file[3]
vRangle = file[4]
xP1 = file[5]
yP1 = file[6]
mP1 = file[7]
xP2 = file[8]
yP2 = file[9]
mP2 = file[10]
xP3 = file[11]
yP3 = file[12]
mP3 = file[13]
xP4 = file[14]
yP4 = file[15]
mP4 = file[16]

sizeX =1000
sizeY = 1000
 
pygame.init()
screen = pygame.display.set_mode([sizeX, sizeY])
 
class Rakieta:
    def __init__(self,xR,yR,vR,mR,angle):
        self.xR = xR
        self.yR = yR
        self.vR = vR
        self.mR = mR
        self.angle = angle
        
    def draw(self,screen,size):
        pygame.draw.circle(screen,(200,70,100),(self.xR,self.yR),size)
       
class Planet:
    def __init__(self,xP,yP,mP) :
        self.xP = xP
        self.yP = yP
        self.mP = mP
    def draw(self,screen,size):
        pygame.draw.circle(screen,(150,0,200),(self.xP,self.yP),size)

def distance (xR,yR,xP,yP):
    return math.sqrt((xR - xP)**2 + (yR - yP)**2)

def gravity (mR , mP ,xR ,yR ,xP,yP):
    G=10
    r=distance(xR,yR,xP,yP)
    return G*(mR*mP)/(r**2)

rakieta = Rakieta(xR, yR, vR, mR, vRangle)
listaP = [
    Planet(xP1, yP1, mP1),
    Planet(xP2, yP2, mP2),
    Planet(xP3, yP3, mP3),
    Planet(xP4, yP4, mP4)
]

running = True
 
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))

    for planet in listaP:
        planet.draw(screen, size=100)

    rakieta.draw(screen,10)

    listaF=[]
    for planet in  listaP:
        F = gravity(rakieta.mR, planet.mP, rakieta.xR, rakieta.yR, planet.xP, planet.yP)
        listaF.append(F)         
    pygame.display.flip()
print(listaF)  

pygame.quit()

