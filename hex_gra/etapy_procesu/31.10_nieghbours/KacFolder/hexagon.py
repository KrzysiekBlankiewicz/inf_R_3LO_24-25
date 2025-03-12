import math
import pygame
import hex 
import pion
import random
pygame.init()
a = 20
offset = 5
radius = 10
a_prime = a + offset/math.sqrt(3)

sizeX =1000
sizeY = 1000

screen = pygame.display.set_mode([sizeX, sizeY])
hexList= []

for q in range(-radius,0):
    for s in range(radius,-radius-q-1,-1):
        hex1 = hex.Hex(q,-q-s,s)
        hexList.append(hex1)
for q in range(0,radius+1):
    for r in range(-radius,radius-q+1):
        hex1 = hex.Hex(q,r,-q-r)
        hexList.append(hex1)
print(hexList)
hex.setSomsiad(hexList)
print("Essa: ",hexList[7].q,hexList[7].r)
for x in hexList[7].somsiad:
    print(x.q,x.r)
    
pion1 = pion.Pion(hexList[0])
running = True
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                s = random.choice(pion1.hex.somsiad)
                s.color = (255,0,0)
                print(s)
                pion1.move(s)
 
    screen.fill((255, 255, 255))
    for h in hexList:
            h.draw(a,a_prime,sizeX,sizeY,screen)
    pion1.draw(screen)
    pygame.display.flip()

pygame.quit()