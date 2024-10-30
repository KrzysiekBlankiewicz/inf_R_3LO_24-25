import math
import pygame
import gra_rysowanie
pygame.init()

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    a = 30
    offset = 5
    radius = 3
 
    for q in range(-radius, radius + 1):
        for r in range(-radius, radius + 1):
            #narysuj hex           
            
                
    pygame.display.flip()

pygame.quit()