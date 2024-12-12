import pygame
import math
pygame.init
def fibonaczi(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonaczi(n-1)+fibonaczi(n-2)

screen = pygame.display.set_mode([1000,1000])

running = True
while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False

    screen.fill((0,0,0))
    black=(0,0,0)
    color=(255, 20, 147)

    pygame.draw.arc(screen,(color),  (700, 700, 600, 600), 10, 20, 1 )


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
