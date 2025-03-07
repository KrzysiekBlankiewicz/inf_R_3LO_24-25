import pygame.draw
import Kolory as k


g_1 = 6.67*10**-11
g_2 = 1

class Rocket:
    def __init__(self, mass, posX, posY):
        self.vel = (0,0)
        self.mass = mass
        self.posX = posX
        self.posY = posY
        self.color = k.white
        self.radius = 7

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.posX, self.posY), self.radius)

    def distance(self, object):
        deltaX = abs(self.posX - object.posX)
        deltaY = abs(self.posY - object.posY)
        realDistance = (deltaX**2 + deltaY**2)**0.5
        return round(realDistance)

    def grav(self, object):
        m1 = self.mass
        m2 = object.mass
        r_2 = self.distance(object)**2
        return round(g_1 * m1 * m2 / r_2)



#pingwin = Rocket(20*10**15, 500, 500)
#pikachu = Rocket(10, 100,400)
#print(pingwin.distance(pikachu))
#print(pingwin.grav(pikachu))
