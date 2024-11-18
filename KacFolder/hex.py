import math
import pygame
import random
def hexagon(q,r,s,a):
    xcord = (a*1/2)*q+a*q
    ycord = s*(math.sqrt(3)*a)/2-r*(math.sqrt(3)*a)/2
    return xcord,ycord

def topleftPosition(x,y,sizeX,sizeY):
    xpos = x + sizeX/2
    ypos = y + sizeY/2
    return xpos,ypos

def vertices(x,y,a):
    v1 = [x-(a/2),y+(a*math.sqrt(3)/2)]
    v2 = [x+(a/2),y+(a*math.sqrt(3)/2)]
    v3 = [x+a,y]
    v4 = [x+(a/2),y-(a*math.sqrt(3)/2)]
    v5 = [x-(a/2),y-(a*math.sqrt(3)/2)]
    v6 = [x-a,y]
    return v1,v2,v3,v4,v5,v6


class Hex:
    def __init__(self,q,r,s) :
        self.somsiad = []
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.q = q
        self.r = r
        self.s = s 
        self.xPos = 0
        self.yPos = 0
        self.beornottobe = ""
    def draw(self,a,a_prime,sizeX,sizeY,screen):
            hexcenter = hexagon(self.q,-self.q-self.s,self.s,a_prime)
            toplefeftpos = topleftPosition(hexcenter[0],hexcenter[1],sizeX,sizeY)
            self.xPos = toplefeftpos[0]
            self.yPos = toplefeftpos[1]
            verticesList = vertices(toplefeftpos[0],toplefeftpos[1],a)
            pygame.draw.polygon(screen,self.color,verticesList)
    def addSomsiad(self,otherHex):
        self.somsiad.append(otherHex)
    def isSomsiad(self,otherHex):
        if self.q == otherHex.q or self.r == otherHex.r or self.s == otherHex.s:
            if otherHex.q == self.q + 1 or otherHex.r == self.r +1 or otherHex.s == self.s + 1:
                self.addSomsiad(otherHex)
    
def setSomsiad(listOfHex):
    somsiad_licz = 0
    for x in listOfHex:
      for y in listOfHex:
          x.isSomsiad(y)
