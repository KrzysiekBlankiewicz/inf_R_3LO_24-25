import pygame
import math
pygame.init()

spiralSize = 1

def fibbonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibbonacci(n-1)+fibbonacci(n-2)

xSize, ySize = 1000, 1000
screen = pygame.display.set_mode((xSize, ySize))
center = (xSize/2, ySize/2)
black = (0,0,0)
white = (255, 255, 255)

screen.fill(white)

quarter = 0

for i in range(0, spiralSize):
    radius = fibbonacci(i)*100
    rect = ((center[0]-radius,center[1]-radius), (center[0]+radius,center[1]+radius))
    pygame.draw.arc(screen, black, rect, quarter * math.pi/2, (quarter+1) * math.pi/2)
    quarter = (quarter + 1)%4

pygame.display.flip()

