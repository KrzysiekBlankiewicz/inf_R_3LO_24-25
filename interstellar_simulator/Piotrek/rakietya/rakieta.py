import math
import pygame
import danerakiety as x

g = 6.67*10**-10
e36 = x.Rakieta(0,3000,300,500,0)
masr = x.Planeta(4171*10**20,300,800,(255,0,0))
g0wn06 = x.Planeta(6231*10**22,800,100,(100,200,10))
k75 = x.Planeta(1111*10**30,100,264,(251,117,255))
listplanet = [masr,g0wn06]

def distancex(pla):
    dysx = e36.posx - pla.posx 
    dysy = e36.posy - pla.posy 
    return dysx , dysy
    
def pitagej(a,b):
    c = math.sqrt(a**2+b**2)
    return c

def silagravitacjix(plax):
    ff15 = g*((e36.mass)*(plax.mass))/(pitagej(distancex(plax)[0],distancex(plax)[1]))**2
    fx = ((distancex(plax)[0])/(pitagej(distancex(plax)[0],distancex(plax)[1])))*ff15*(-0.0000000001)/100
    fy = ((distancex(plax)[1])/(pitagej(distancex(plax)[0],distancex(plax)[1])))*ff15*(-0.0000000001)/100
    return fx,fy

pygame.init()
screen = pygame.display.set_mode([1000, 1000])
clock = pygame.time.Clock()
running = True

ax = 0
ay = 0
vx = 0
vy = 0
    
while running:

    clock.tick(60)
    fwx = 0
    fwy = 0
    
    screen.fill((0, 0, 0))  

    
    pygame.draw.circle(screen,(0,255,0),(e36.posx,e36.posy),5)
    for p in listplanet:
            pygame.draw.circle(screen,(p.color),(p.posx,p.posy),50)
            pygame.draw.line(screen,(20,20,255),(e36.posx,e36.posy),((e36.posx+silagravitacjix(p)[0]),(e36.posy+silagravitacjix(p)[1])))
            fwy = fwy + silagravitacjix(p)[1]
            fwx = fwx + silagravitacjix(p)[0]
            pygame.draw.line(screen,(97,24,255),(e36.posx,e36.posy),((e36.posx+silagravitacjix(p)[0]),(e36.posy+silagravitacjix(p)[1])))
    pygame.draw.line(screen,(0,20,255),(e36.posx,e36.posy),((e36.posx+fwx),(e36.posy+fwy)))
    ax = fwx/e36.mass
    ay = fwy/e36.mass
    e36.velocityx = (0 - ax)*20
    e36.velocityx = (0 - ay)*20
    e36.posx = e36.posx + e36.velocityx
    e36.posy = e36.posy + e36.velocityy
    pygame.display.flip()
for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

pygame.quit()