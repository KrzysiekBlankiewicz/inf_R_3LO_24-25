import pygame
import math
def fib(n):
    if n== 1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(6))

pygame.init()


sizeX =1000
sizeY = 1000

screen = pygame.display.set_mode([sizeX, sizeY])

running = True
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.draw.arc(screen,(100,100,100),((100,700),(500,500)),0,math.pi/2)
    pygame.draw.arc(screen,(100,100,100),((100,100),(500,500)),-math.pi/2,0)
    pygame.display.flip()

pygame.quit()