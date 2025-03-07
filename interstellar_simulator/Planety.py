import pygame.draw
import Kolory as k

class Planet:
    def __init__(self, mass, posX, posY, color, radius):
        self.mass = mass
        self.posX = posX
        self.posY = posY
        self.color = color
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.posX, self.posY), self.radius)




