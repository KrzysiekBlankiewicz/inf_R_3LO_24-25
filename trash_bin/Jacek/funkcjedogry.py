import math
import pygame

color = (150, 0,200)

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


class Hex:
    def __init__(self, q, r, s):
        self.q = q
        self.r = r
        self.s = s
        self.neighbours = []
        
    def addNeighbour(self, innyhex):
        if innyhex not in self.neighbours:
            self.neighbours.append(innyhex)
            


    def draw(self, a, A, middle, screen):
        hexFromCenterPosition = position(self.q, self.r, self.s, A)
        properPosition = topLeftPosition(hexFromCenterPosition, middle)
        verticesList = vertices(properPosition, a)
        pygame.draw.polygon(screen, color, verticesList)

    def pawnPosition(self, A, middle):
        hexFromCenterPosition = position(self.q, self.r, self.s, A)
        properPosition = topLeftPosition(hexFromCenterPosition, middle)
        return properPosition
    
    def isNeighbour(self, innyhex):
        if self.q == innyhex.q and abs(self.r - innyhex.r) == 1 and abs(self.s - innyhex.s) == 1:
            return 1
        if self.r == innyhex.r and abs(self.q - innyhex.q) == 1 and abs(self.s - innyhex.s) == 1:
            return 1
        if self.s == innyhex.s and abs(self.r - innyhex.r) == 1 and abs(self.q - innyhex.q) == 1:
            return 1
        return 0

def setNeighbourhood(hexy):
    for a in hexy:
        for b in hexy:
            if a.isNeighbour(b) == 1:
                a.addNeighbour(b)
                b.addNeighbour(a)
