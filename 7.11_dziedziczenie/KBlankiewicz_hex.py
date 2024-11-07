import math
import pygame

red = (255, 0, 0)
blue = (0, 0, 255)

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
        self.occupied = False
        
    def addNeighbour(self, otherHex):
        if otherHex not in self.neighbours:
            self.neighbours.append(otherHex)

    def draw(self, a, a_prime, middle, screen):
        hexFromCenterPosition = position(self.q, self.r, self.s, a_prime)
        properPosition = topLeftPosition(hexFromCenterPosition, middle)
        verticesList = vertices(properPosition, a)
        if self.occupied:
            pygame.draw.polygon(screen, red, verticesList)
        else:
            pygame.draw.polygon(screen, blue, verticesList)

    def pawnPosition(self, a_prime, middle):
        hexFromCenterPosition = position(self.q, self.r, self.s, a_prime)
        properPosition = topLeftPosition(hexFromCenterPosition, middle)
        return properPosition
    
    def isNeighbour(self, otherHex):
        if self.q == otherHex.q and abs(self.r - otherHex.r) == 1 and abs(self.s - otherHex.s) == 1:
            return True
        elif self.r == otherHex.r and abs(self.q - otherHex.q) == 1 and abs(self.s - otherHex.s) == 1:
            return True
        elif self.s == otherHex.s and abs(self.r - otherHex.r) == 1 and abs(self.q - otherHex.q) == 1:
            return True
        else:
            return False
    def addPawn(self, pawn):
        if self.occupied == False:
            self.occupied = True
            self.pawn = pawn

def setNeighbourgood(hexes):
    for a in hexes:
        for b in hexes:
            if a.isNeighbour(b):
                a.addNeighbour(b)
                b.addNeighbour(a)
