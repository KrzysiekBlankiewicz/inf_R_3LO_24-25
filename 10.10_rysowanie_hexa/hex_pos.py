import math
import pygame
pygame.init()

def position(q, r, s, a):
    if q + r + s != 0:
        return False
    xPos = q * (1.5 * a)
    yPos = (s - r) * (a * math.sqrt(3) )/2

    return (xPos, yPos)

def topLeftPosition(hexPosFromCenter, screenCenter):
    xPos = hexPosFromCenter[0] + screenCenter[0]
    yPos = hexPosFromCenter[1] + screenCenter[1]
    return (xPos, yPos)

def vertices(position, a):
    x = position[0]
    y = position[1]
    v1 = (x - a/2, y + (a * math.sqrt(3))/2 )
    v2 = (x + a/2, y + (a * math.sqrt(3))/2 )
    v3 = (x + a, y)
    v4 = (x + a/2, y - (a * math.sqrt(3))/2 )
    v5 = (x - a/2, y - (a * math.sqrt(3))/2 )
    v6 = (x - a, y)
    return [v1, v2, v3, v4, v5, v6]

#wartości zmiennych
a = 50
screenHeight = 600
screenWidth = 600
middle = (screenWidth/2, screenHeight/2)
screen = pygame.display.set_mode([screenWidth, screenHeight])
red = (255, 0, 0)

#hex do narysowania
q = 0
r = 0
s = 0

#wyznacz pozycję mojego hexa względem środka planszy
hexFromCenterPosition = position(0, 0, 0, a)

#wyznacz pozycję względem lewego górnego rogu (pyGame tego wymaga)
properPosition = topLeftPosition(hexFromCenterPosition, middle)

#wyznacz wierzchołki hexa
vertices = vertices(properPosition, a)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #wypełnij ekran bielą
    screen.fill((255, 255, 255))
    #narysuj hex
    pygame.draw.polygon(screen, red, vertices)

    #pokaż na ekranie narysowaną zawartość
    pygame.display.flip()

pygame.quit()

