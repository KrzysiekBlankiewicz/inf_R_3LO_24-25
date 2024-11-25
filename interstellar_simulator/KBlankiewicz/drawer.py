
import pygame

pygame.init()
screenHeight = 1000
screenWidth = 1000
screen = pygame.display.set_mode([screenWidth, screenHeight])

def drawLine():
    pass
def drawCircle(x, y, r, color):
    pygame.draw.circle(screen, color, (x, y), r)
