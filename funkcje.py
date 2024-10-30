import math
import pygame

def hexagon(q, r, s, a, offset):
    a = a + offset / math.sqrt(3)
    xcord = (a * 1 / 2) * q + a * q
    ycord = s * (math.sqrt(3) * a) / 2 - r * (math.sqrt(3) * a) / 2
    return xcord, ycord

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

class Hex:
    neighbours = []
    def __init__(self,q,r,s) :
        self.q = q
        self.r = r
        self.s = s
    def addSomsiad(self,otherhex):
        self.neighbours.append(otherhex)
    def draw(self,a,A,sizeX,sizeY,screen):
            hexcenter = hexagon(self.q,-self.q-self.s,self.s,A)
            toplefeftpos = topleftPosition(hexcenter[0],hexcenter[1],sizeX,sizeY)
            verticesList = vertices(toplefeftpos[0],toplefeftpos[1],a)
            pygame.draw.polygon(screen,(255,0,0),verticesList)
