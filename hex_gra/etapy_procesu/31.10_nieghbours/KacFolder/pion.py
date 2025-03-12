import pygame
import math
import hex
import random

class Pion:
    def __init__(self, hex):
        self.hex = hex
    def draw(self, screen):
        pygame.draw.circle(screen,(200,0,0),(self.hex.xPos,self.hex.yPos),10)
    def move(self, gdziedzbanie):
        self.hex = gdziedzbanie
    