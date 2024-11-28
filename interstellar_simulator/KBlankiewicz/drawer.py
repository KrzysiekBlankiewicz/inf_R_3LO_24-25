import pygame

screenHeight = 1000
screenWidth = 1000

def init():
    pygame.init()
    global screen
    screen = pygame.display.set_mode([screenWidth, screenHeight])
def drawLine(start, end, color):
    pygame.draw.line(screen, color, start, end)
def drawCircle(x, y, r, color):
    pygame.draw.circle(screen, color, (x, y), r)
def flip():
    pygame.display.flip()

