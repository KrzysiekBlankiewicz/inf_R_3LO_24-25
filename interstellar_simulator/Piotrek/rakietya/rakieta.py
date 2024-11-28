import math
import pygame
import danerakiety as x

g = 6.67*10**-10
e36 = x.Rakieta(300,5000,30,500,200)
masr = x.Planeta(4171*10**23,300,800,(255,0,0))
g0wn06 = x.Planeta(6231*10**22,800,100,(100,200,10))

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
    fx = math.cos(math.acos((distancex(plax)[0])/(pitagej(distancex(plax)[0],distancex(plax)[1]))))*ff15*(-0.0000000001)/1000
    fy = math.sin(math.asin((distancex(plax)[1])/(pitagej(distancex(plax)[0],distancex(plax)[1]))))*ff15*(-0.0000000001)/1000
    return fx,fy
     
     


pygame.init()
screen = pygame.display.set_mode([1000, 1000])
clock = pygame.time.Clock()
running = True
 
while running:
    clock.tick(60)
    print(clock)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))  

        pygame.draw.circle(screen,(0,255,0),(e36.posx,e36.posy),5)
        for p in listplanet:
            pygame.draw.circle(screen,(p.color),(p.posx,p.posy),50)
            pygame.draw.line(screen,(20,20,255),(e36.posx,e36.posy),((e36.posx+silagravitacjix(p)[0]),(e36.posy+silagravitacjix(p)[1])))
        pygame.display.flip()


pygame.quit()
