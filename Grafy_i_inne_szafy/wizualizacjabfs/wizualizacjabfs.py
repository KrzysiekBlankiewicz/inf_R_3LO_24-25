import math
import pygame
import funkcjedogry
import pionek
import bfs

pygame.init()
 

a = 30
offset = 5
A = a + offset / math.sqrt(3)
screenY = 500
screenX = 500
radius = 3
middle = (screenX/2, screenY/2)
screen = pygame.display.set_mode([screenX, screenY])

listahexy = []

for q in range(-radius, radius + 1):
        for r in range(-radius, radius + 1):
            s = -q - r
            if abs(q) + abs(r) + abs(s) <= radius * 2:
                hex1 = funkcjedogry.Hex(q, -q-s, s)
                listahexy.append(hex1)

funkcjedogry.setNeighbourhood(listahexy)

 
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))

    for h in listahexy:
        h.draw(a, A, middle, screen)
    
    pygame.display.flip()
    
pygame.quit()
