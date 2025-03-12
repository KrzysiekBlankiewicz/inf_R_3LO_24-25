#by Jozek
import pygame
import math
import hexy_alfa

Ile_Hex_y = 20
ile_hex_x = 15
q = 0
r = 0
s = 0
num_sides = 6

White = (255, 255, 255)
Green = (0, 255, 0)
Black = (0, 0, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)
kolor_hex = Red

pygame.init()

size = (1900, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hex Drawing")



done = False
# Main program loop
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # --- Game logic should go here
            # --- Drawing code should go here
    screen.fill(White)

    for j in range(0,Ile_Hex_y):
        
        for q in range(0,ile_hex_x):
            r= -q
            hex1 = hexy_alfa.Hex(q,r,s)
            hex1.draw(j,size,screen)
            
        for r in range(0,ile_hex_x):
            q = -r
            hex1 = hexy_alfa.Hex(q,r,s)
            hex1.draw(j,size,screen)
            
                    # --- Go ahead and update the screen with what we've drawn
    pygame.display.flip()
        
            
pygame.quit()
 

