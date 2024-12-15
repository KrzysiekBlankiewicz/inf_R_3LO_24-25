import pygame
import math
def Fibo(n):
    liczby_fibo = []
    if n == 1:
        liczby_fibo = [1]
    else:
        liczby_fibo = [1, 1]
        for i in range(2, n):
            liczby_fibo.append(liczby_fibo[i-2] + liczby_fibo[i-1])
    return liczby_fibo


pygame.init()


sizeX =1000
sizeY = 1000

screen = pygame.display.set_mode([sizeX, sizeY])

running = True
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
    pygame.draw.rect(screen,(0,0,100),((0,0),(400,400)))
    pygame.draw.rect(screen,(0,0,200),((400,0),(250,250)))
    pygame.draw.rect(screen,(0,0,200),((500,250),(150,150)))
    pygame.draw.rect(screen,(0,0,250),((400,300),(100,100)))
    pygame.draw.rect(screen,(200,200,250),((400,250),(50,50)))
    pygame.draw.rect(screen,(150,200,250),((450,250),(50,50)))
    #pygame.draw.arc(screen,(100,255,100),((0,0),(800,800)),math.pi/2,math.pi)
    #pygame.draw.arc(screen,(200,0,0),((200,0),(450,500)),2*math.pi,math.pi/2)
    #pygame.draw.arc(screen,(100,0,0),((350,100),(300,300)),(3/2)*math.pi,2*math.pi)
    #pygame.draw.arc(screen,(255,0,0),((400,200),(200,200)),math.pi,(3/2)*math.pi)
    #pygame.draw.arc(screen,(255,255,0),((400,250),(100,100)),math.pi/2,math.pi)
    #pygame.draw.arc(screen,(255,150,0),((400,250),(100,100)),2*math.pi,math.pi/2)
    cykl = 1
    x= 0
    y=0
    n=6
    skala = 100
    lista= Fibo(n)
    print(lista)
    for xd in range(len(lista)-1,-1,-1):
        if cykl ==1:
            pygame.draw.arc(screen,(100,255,50),((x,y),(lista[xd]*skala,lista[xd]*skala)),math.pi/2,math.pi)
            x=x+((lista[xd]*skala)/2)-((skala*lista[xd-1])/2)
            #print(x)
        if cykl ==2:
            pygame.draw.arc(screen,(200,0,0),((x,y),(lista[xd]*skala,lista[xd]*skala)),2*math.pi,math.pi/2)
            y+=skala*lista[xd]/2-(skala*(lista[xd-1])/2)
            x=x+lista[xd]*skala-(skala*(lista[xd-1]))
        if cykl ==3:
            pygame.draw.arc(screen,(100,0,0),((x,y),(lista[xd]*skala,lista[xd]*skala)),(3/2)*math.pi,2*math.pi)
            x=x+((skala*lista[xd])/2)-(skala*(lista[xd-1]/2))
            y=y+(skala*lista[xd])-(skala*(lista[xd-1]))
            #print(x,y)
        if cykl==4:
            pygame.draw.arc(screen,(255,255,0),((x,y),(lista[xd]*skala,lista[xd]*skala)),math.pi,(3/2)*math.pi)
            y=y+skala*lista[xd]/2-(skala*(lista[xd-1])/2)
        if cykl == 4:
            cykl =1 
        else: 
            cykl+=1
        

    pygame.display.flip()

pygame.quit()
