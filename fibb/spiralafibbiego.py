import pygame
import math
pygame.init()

#dane
xsize=1000
ysize=1000
colorarc=(100,0,200)
color=(0,0,255)

#funkcje
def fibo(n):
    if n==1 or n==2:
        output=1
    else:
        output = fibo(n-1) + fibo(n-2)
    return output

f = []

for n in range (1,10):
        n=fibo(n)
        f.append(n)

screen = pygame.display.set_mode((xsize,ysize))
screen.fill((255,255,255))
X=xsize/2
Y=ysize/2
P1=math.pi
P2=math.pi
a=10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(color)
    pygame.draw.arc(screen, colorarc, ((X,Y),(-a*f[1],-a*f[1])),P1*(2/4),P2,5)
    pygame.draw.arc(screen, colorarc, ((X,Y),(a*f[1],a*f[1])),P1*(2/4),P2,5)
    pygame.draw.arc(screen, colorarc, ((X-1/2*a,Y),(a*f[2],a*f[2])),P1*2,P2/2,5)
    pygame.draw.arc(screen, colorarc, ((X-3/2*a,Y-1/2*a),(a*f[3],a*f[3])),P1*(3/2),P2*2,5)
    pygame.draw.arc(screen, colorarc, ((X-5/2*a,Y-5/2*a),(a*f[4],a*f[4])),P1,P2*(3/2),5)
    pygame.draw.arc(screen, colorarc, ((X-5/2*a,Y-4*a),(a*f[5],a*f[5])),P1/2,P2,5)
    pygame.draw.arc(screen, colorarc, ((X-5*a,Y-4*a),(a*f[6],a*f[6])),P1*0,P2/2,5)
    #for i in f:
        #pygame.draw.arc(screen, colorarc, ((X-,Y),(a*i,a*i)),P1/2,P2,5)
        

    

    pygame.display.flip()
pygame.quit()


