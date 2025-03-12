import math
import pygame
import hexagon
pygame.init()
 
xrozmiar=1000
yrozmiar=1000
a=80
offset=3
xcenter=xrozmiar/2
ycenter=yrozmiar/2
screen = pygame.display.set_mode((xrozmiar, yrozmiar))
WHITE = (0,0,0)
B=10
BLUE = (B, B, B)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the hexagon
    
    q = 0
    radius = 3
    for q in range(0, radius+1):
        for r in range(-radius, radius+1-q):
            hexa=hexagon.Hexagon(q,r,-q-r)
            hexa.rysuj_hex(xcenter,ycenter,a, offset, screen, BLUE)
            B+=5
            BLUE = (B, B, B)
    for q in range(-radius, 0):
        for s in range(radius, -radius-q-1,-1):
            hexa2=hexagon.Hexagon(q,-q-s,s)
            hexa2.rysuj_hex(xcenter,ycenter,a, offset, screen, BLUE)
            B+=5
            BLUE = (B, B, B)


    pygame.display.flip()
pygame.quit()

 
 



