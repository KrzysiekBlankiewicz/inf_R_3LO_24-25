import math
import pygame
pygame.init()

def hexagon(q, r, s, a, offset):
    a = a + offset / math.sqrt(3)
    xcord = (a * 1 / 2) * q + a * q
    ycord = s * (math.sqrt(3) * a) / 2 - r * (math.sqrt(3) * a) / 2
    return xcord, ycord

sizeX = 500
sizeY = 500

def topleftPosition(x, y):
    xpos = x + sizeX / 2
    ypos = y + sizeY / 2
    return xpos, ypos

def vertices(x, y):
    v1 = [x - (a / 2), y + (a * math.sqrt(3) / 2)]
    v2 = [x + (a / 2), y + (a * math.sqrt(3) / 2)]
    v3 = [x + a, y]
    v4 = [x + (a / 2), y - (a * math.sqrt(3) / 2)]
    v5 = [x - (a / 2), y - (a * math.sqrt(3) / 2)]
    v6 = [x - a, y]
    return v1, v2, v3, v4, v5, v6

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 0, 0))
    a = 20
    offset = 10
    radius = 3

    # Dla q i r w promieniu rysuj
    for q in range(-radius, radius + 1):
        for r in range(-radius, radius + 1):
            s = -q - r
            # Rysuj tylko w zakresie promienia
            if abs(q) + abs(r) + abs(s) <= radius * 2:
                hexcenter = hexagon(q, r, s, a, offset)
                topleftpos = topleftPosition(hexcenter[0], hexcenter[1])
                verticesList = vertices(topleftpos[0], topleftpos[1])
                pygame.draw.polygon(screen, (150, 0, 255), verticesList)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
