import math
import pygame
import funkcjedogry
import pionek

pygame.init()
 

a = 30
offset = 5
A = a + offset / math.sqrt(3)
screenY = 500
screenX = 500
radius = 3
middle = (screenX/2, screenY/2)
screen = pygame.display.set_mode([screenX, screenY])
pionekrozmiar = 20

listahexy = []

for q in range(-radius, radius + 1):
        for r in range(-radius, radius + 1):
            s = -q - r
            if abs(q) + abs(r) + abs(s) <= radius * 2:
                hex1 = funkcjedogry.Hex(q, -q-s, s)
                listahexy.append(hex1)

funkcjedogry.setNeighbourhood(listahexy)

player = pionek.pawn(listahexy[0])

 
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.randomruch()
            if event.key == pygame.K_a:
                player.randomruch()
            if event.key == pygame.K_d:
                player.randomruch()

    screen.fill((255, 255, 255))

    for h in listahexy:
        h.draw(a, A, middle, screen)

    player.draw(A, middle, screen, pionekrozmiar)
    
    pygame.display.flip()
    
pygame.quit()
