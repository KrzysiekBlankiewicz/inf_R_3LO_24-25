import math
import pygame
import random
class Planet:
    def __init__(self,planetx,planety,planetM) :
        self.planetx = planetx
        self.planety = planety
        self.mass = planetM
    def draw(self,screen,size):
        pygame.draw.circle(screen,(200,0,0),(self.planetx,self.planety),size)