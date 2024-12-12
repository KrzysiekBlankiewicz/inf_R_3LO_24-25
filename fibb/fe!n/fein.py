import math
import pygame

screen = pygame.display.set_mode([1000, 1000])
def fibonaci(n):
    if n ==1 or n == 2:
        return 1 
    return fibonaci(n-2) + fibonaci(n-1)


def rysudein():
    pygame.draw.arc(screen,(100,100,100),((200,200),(100,100)),0,math.pi/2)


pygame.init()
clock = pygame.time.Clock()
running = True







while running:
    
    screen.fill((0, 0, 0))  
    pygame.draw.arc(screen,(100,100,100),((200,200),(50,50)),0,math.pi)    
    
    
    
    
    
    
    
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

pygame.quit()