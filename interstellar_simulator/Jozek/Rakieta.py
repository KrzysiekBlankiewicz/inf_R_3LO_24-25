import pygame.draw
import Kolory as k

g = 6.67*10**-11

class Rocket:
    def __init__(self, mass, posX, posY):
        self.vel = (0,0)
        self.mass = mass
        self.posX = posX
        self.posY = posY
        self.velX = 0
        self.velY = 0
        self.accX =0
        self.accY = 0
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
        return round(g * m1 * m2 / r_2)

    def draw_Fwyp(self, screen, FwypX, FwypY):
        pygame.draw.line(screen, k.green, (self.posX, self.posY), (self.posX + FwypX, self.posY + FwypY), 2)

    def move(self):
        self.posX += self.velX
        self.posY += self.velY

    def velocity(self):
        self.velX += self.accX
        self.velY += self.accY

    def acceleration(self, FwypX, FwypY):
        self.accX = FwypX / self.mass
        self.accY = FwypY / self.mass
