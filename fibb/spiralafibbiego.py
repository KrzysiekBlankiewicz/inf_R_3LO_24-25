import pygame
import math

pygame.init()

color=(0,0,0)
screen = pygame.display.set_mode((1000,1000))
screen.fill(color)

colorarc=(100,0,200)
rect=((0,0),(500,500))

def fibo(n):
    if n==1 or n==2:
        output=1
    else:
        output = fibo(n-1) + fibo(n-2)
    return output

fibonumlist = []
def fibonum(n):
    for n in range (1,10):
        n=fibo(n)
        fibonumlist.append(n)

print(fibonumlist)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
            

