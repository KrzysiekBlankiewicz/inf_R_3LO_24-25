import pygame
import random
import time
import Kolory as k

g = 6.67*10**-12 #Zwiększyłem potęgę z 11 do 12, żeby ładniej wyglądało to na symulacji

class Rocket:
    def __init__(self, mass, posX, posY, vel, acc):
        self.vel = (0,0)
        self.mass = mass
        self.posX = posX
        self.posY = posY
        self.velX = vel
        self.velY = vel
        self.accX = acc
        self.accY = acc
        self.color = k.white
        self.radius = 5

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.posX, self.posY), self.radius)

    def distance(self, object):
        deltaX = abs(self.posX - object.posX)
        deltaY = abs(self.posY - object.posY)
        realDistance = (deltaX**2 + deltaY**2)**0.5
        return (realDistance)

    def grav(self, object):
        m1 = self.mass
        m2 = object.mass
        r_2 = self.distance(object)**2
        return (g * m1 * m2 / r_2)

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

    def teleport_start(self, screen):
        pygame.draw.circle(screen, k.light_blue, (self.posX, self.posY), 20)
        pygame.draw.circle(screen, k.white, (self.posX, self.posY), 2)
        pygame.display.update()
        time.sleep(0.3)
        pygame.draw.circle(screen, k.white, (self.posX, self.posY), 7)
        pygame.display.update()
        time.sleep(0.3)
        pygame.draw.circle(screen, k.white, (self.posX, self.posY), 12)
        pygame.display.update()

    def teleport_end(self, screen):
        pygame.draw.circle(screen, k.light_blue, (self.posX, self.posY), 20)
        pygame.draw.circle(screen, k.white, (self.posX, self.posY), 2)
        pygame.display.update()
        time.sleep(0.3)
        pygame.draw.circle(screen, k.white, (self.posX, self.posY), 7)
        pygame.display.update()
        time.sleep(0.3)
        pygame.draw.circle(screen, k.white, (self.posX, self.posY), 12)
        pygame.display.update()
        time.sleep(1)

    def teleport(self):
        self.accX = 0
        self.accY = 0
        self.velX = 0
        self.velY = 0
        self.posX = random.randrange(200,1700)
        self.posY = random.randrange(200, 800)