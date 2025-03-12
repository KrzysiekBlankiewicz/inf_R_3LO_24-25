import math
import pygame
import hex
pygame.init()
a = 30
offset = 5
a_prime = a + offset/math.sqrt(3)

sizeX = 500
sizeY = 500

screen = pygame.display.set_mode([500, 500])
 
running = True
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    screen.fill((255, 255, 255))
    radius = 3
    for q in range(-radius,0):
        for s in range(radius,-radius-q-1,-1):
            hex1 = hex.Hex(q,-q-s,s)
            hex1.draw(a,a_prime,sizeX,sizeY,screen)
    for q in range(0,radius+1):
        for r in range(-radius,radius-q+1):
            hex1 = hex.Hex(q,r,-q-r)
            hex1.draw(a,a_prime,sizeX,sizeY,screen)
 
    pygame.display.flip()
 
pygame.quit()