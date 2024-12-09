import math
import pygame

class rakieta:
    def __init__(self,velocity,mass,angle,posx,posy):
        self.velocity = velocity
        self.mass = mass
        self.angle = angle
        self.posx = posx
        self.posy = posy
        
        self.velocityx = velocity*math.cos(self.angle)
        self.velocityy = velocity*math.sin(self.angle)
class planeta:
    def __init__(self,mass,posx,posy):
        self.mass = mass
        self.posx = posx
        self.posy = posy
        
