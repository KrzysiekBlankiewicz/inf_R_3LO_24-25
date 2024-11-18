Dane=open('dane.txt').read().splitlines()
import math
import pygame

screen = pygame.display.set_mode((1000,1000))

for i in range(len(Dane)):
    Dane[i]=int(Dane[i])

xRakiety=Dane[0]
yRakiety=Dane[1]
masaRakiet=Dane[2]
kątRakiety=Dane[3]
prędkośćRakiety=Dane[4]

xPlanety1=Dane[5]
yPlanety1=Dane[6]
masaPlanety1=Dane[7]

xPlanety2=Dane[8]
yPlanety2=Dane[9]
masaPlanety2=Dane[10]

xPlanety3=Dane[11]
yPlanety3=Dane[12]
masaPlanety3=Dane[13]

running = True
while running:

    screen.fill((0,0,0))

    pygame.draw.circle(screen,(250,250,250), (xRakiety, yRakiety), 10)
    pygame.draw.circle(screen,(250,0,0), (xPlanety1, yPlanety1), 30)
    pygame.draw.circle(screen,(0,0,250), (xPlanety2, yPlanety2), 50)
    pygame.draw.circle(screen,(0,250,0), (xPlanety3, yPlanety3), 40)
    
    
        

    pygame.display.flip()

pygame.quit()
