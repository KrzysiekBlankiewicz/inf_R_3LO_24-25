import pygame
import math
import random

pygame.init()

# dane
xsize = 1000
ysize = 1000

# funkcje
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

f = []

f = [fibo(n) for n in range(1, 20)]


screen = pygame.display.set_mode((xsize, ysize))
screen.fill((255, 255, 255))

a = 10
katy = [math.pi/2, math.pi, math.pi*3/2, 2*math.pi]  
 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    X = xsize / 2
    Y = ysize / 2
    ile = 0 
    screen.fill((0, 0, 0))
    
    for i in range(len(f)):
        if ile == 0:
            if i ==0:
                pygame.draw.arc(screen,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)),(X, Y, 2*a*f[i],2*a*f[i]),katy[ile],katy[(ile + 1) % 4],3)
                pygame.draw.rect(screen,(255,255,255),(X, Y,2*a*f[i],2*a*f[i]),width=2)
            else:
                Y=Y
                X=X+a*f[i-1]-a*f[i]
                pygame.draw.arc(screen,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)),(X, Y, 2*a*f[i],2*a*f[i]),katy[ile],katy[(ile + 1) % 4],3)
                pygame.draw.rect(screen,(255,255,255),(X, Y,2*a*f[i],2*a*f[i]),width=2)
                
        elif ile == 1:
            X=X
            Y=Y+a*f[i-1]-a*f[i]
            pygame.draw.arc(screen,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)),(X, Y, 2*a*f[i],2*a*f[i]),katy[ile],katy[(ile + 1) % 4],3)
            pygame.draw.rect(screen,(255,255,255),(X, Y,2*a*f[i],2*a*f[i]),width=2)
        elif ile == 2:
            X=X+a*f[i-1]-a*f[i]
            Y=Y-(a*f[i]-a*f[i-1])*2
            pygame.draw.arc(screen,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)),(X, Y, 2*a*f[i],2*a*f[i]),katy[ile],katy[(ile + 1) % 4],3)
            pygame.draw.rect(screen,(255,255,255),(X, Y,2*a*f[i],2*a*f[i]),width=2)
        elif ile == 3:
            Y=Y+a*f[i-1]-a*f[i]
            X=X-(a*f[i]-a*f[i-1])*2
            pygame.draw.arc(screen,(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)),(X, Y, 2*a*f[i],2*a*f[i]),katy[ile],katy[(ile + 1) % 4],3)
            pygame.draw.rect(screen,(255,255,255),(X, Y,2*a*f[i],2*a*f[i]),width=2)       

        ile = (ile + 1) % 4
    

    pygame.display.flip()
    pygame.time.wait(500)

pygame.quit()


