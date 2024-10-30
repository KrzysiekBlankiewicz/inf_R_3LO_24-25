import math
import pygame

sizeX = 500
sizeY = 500

class Hex:
    neighbours = []
    def __init__(self, q, r, s):
        self.q = q
        self.r = r
        self.s = s
    
    def addneighbour(self, otherHex):
        self.neighbours.append(otherHex)

    def draw(self):
        self.s = -self.q - self.r
        if abs(self.q) + abs(self.r) + abs(self.s) <= self.radius * 2:    
            hexcenter = hexagon(self.q, self.r, self.s, self.a, self.offset)
            topleftpos = topleftPosition(hexcenter[0], hexcenter[1])
            verticesList = vertices(topleftpos[0], topleftpos[1])
            pygame.draw.polygon(screen, (0, 0, 0), verticesList)


# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
screen.fill((255, 255, 255))

def hexagon(q, r, s, a, offset):
    a = a + offset / math.sqrt(3)
    xcord = (a * 1 / 2) * q + a * q
    ycord = s * (math.sqrt(3) * a) / 2 - r * (math.sqrt(3) * a) / 2
    return xcord, ycord
 
def topleftPosition(x, y):
    xpos = x + sizeX / 2
    ypos = y + sizeY / 2
    return xpos, ypos

def vertices(x, y, a):
    v1 = [x - (a / 2), y + (a * math.sqrt(3) / 2)]
    v2 = [x + (a / 2), y + (a * math.sqrt(3) / 2)]
    v3 = [x + a, y]
    v4 = [x + (a / 2), y - (a * math.sqrt(3) / 2)]
    v5 = [x - (a / 2), y - (a * math.sqrt(3) / 2)]
    v6 = [x - a, y]
    return v1, v2, v3, v4, v5, v6