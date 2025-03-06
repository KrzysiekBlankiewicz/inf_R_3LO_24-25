import math
import pygame
import abibliotek
import autyzmgrymt

sizeX = 1000
sizeY = 1000


pygame.init()
a = 50
ofe = 5
ape = a + ofe/math.sqrt(3)
screen = pygame.display.set_mode([1000, 1000])
mid = (sizeX/2, sizeY/2)
running = True
radius = 4
hexlist = []

for q in range(-radius,0):
    for s in range(radius,-radius-q-1,-1):
        hex1 = abibliotek.hexik(q,-q-s,s)
        hexlist.append(hex1)
for q in range(0,radius+1):
    for r in range(-radius,radius-q+1):
        hex1 = abibliotek.hexik(q,r,-q-r)
        hexlist.append(hex1)
while running:


 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))    
    for k in hexlist:
        k.draw(a,ape,screen,sizeX,sizeY,(0,255,20))
    pygame.display.flip()
 

pygame.quit()