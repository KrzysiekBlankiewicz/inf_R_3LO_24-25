import math
import pygame

class Rakieta:
    def __init__(self,velocity,mass,angle,posx,posy):
        self.velocity = velocity
        self.mass = mass
        self.angle = angle
        self.posx = posx
        self.posy = posy
        self.velocityx = velocity*math.cos(self.angle)
        self.velocityy = velocity*math.sin(self.angle)

class Planeta:
    def __init__(self,mass,posx,posy,color):
        self.mass = mass
        self.posx = posx
        self.posy = posy
        self.color = color    
