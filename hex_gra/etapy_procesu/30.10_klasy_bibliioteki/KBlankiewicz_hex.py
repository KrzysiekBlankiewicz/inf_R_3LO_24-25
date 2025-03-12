import math
import pygame

red = (255, 0, 0)

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
    neighbours = []
    def __init__(self, q, r, s):
        self.q = q
        self.r = r
        self.s = s
        
    def addNeighbour(self, otherHex):
        self.neighbours.append(otherHex)

    def draw(self, a, a_prime, middle, screen):
        hexFromCenterPosition = position(self.q, self.r, self.s, a_prime)
        properPosition = topLeftPosition(hexFromCenterPosition, middle)
        verticesList = vertices(properPosition, a)
        pygame.draw.polygon(screen, red, verticesList)
    
