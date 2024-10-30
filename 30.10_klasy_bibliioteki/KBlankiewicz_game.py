import math
import pygame
import hex

pygame.init()

#wartości zmiennych
a = 50
offset = 10
a_prime = a + offset / math.sqrt(3)
screenHeight = 1000
screenWidth = 1000
radius = 3
middle = (screenWidth/2, screenHeight/2)
screen = pygame.display.set_mode([screenWidth, screenHeight])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for q in range(-radius, 0):
        for s in range(radius, -radius-q-1, -1):
            hex1 = hex.Hex(q, -q-s, s)
            hex1.draw(a, a_prime, middle, screen)
            
    for q in range(0, radius+1):
        for r in range(-radius, radius-q+1):
            hex2 = hex.Hex(q, r, -q-r)
            hex2.draw(a, a_prime, middle, screen)

    pygame.display.flip()

pygame.quit()

