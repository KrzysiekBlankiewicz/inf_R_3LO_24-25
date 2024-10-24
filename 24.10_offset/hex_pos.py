import math
import pygame

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


pygame.init()

#wartości zmiennych
a = 50
offset = 10
a_prime = a + offset / math.sqrt(3)
screenHeight = 600
screenWidth = 600
middle = (screenWidth/2, screenHeight/2)
screen = pygame.display.set_mode([screenWidth, screenHeight])
red = (255, 0, 0)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #wypełnij ekran bielą
    screen.fill((255, 255, 255))
    #narysuj hex
    q = 0
    radius = 3
    for r in range(-radius, radius):
        hexFromCenterPosition = position(q, r, -q-r, a_prime)
        properPosition = topLeftPosition(hexFromCenterPosition, middle)
        verticesList = vertices(properPosition, a)
        pygame.draw.polygon(screen, red, verticesList)

    #pokaż na ekranie narysowaną zawartość
    pygame.display.flip()

pygame.quit()

