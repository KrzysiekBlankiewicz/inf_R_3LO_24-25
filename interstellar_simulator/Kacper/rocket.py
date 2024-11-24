import pygame
import math
import random
class Rocket:
    def __init__(self,rocketx,rockety,velocity,rocketM,rocketA):
        self.rocketx = rocketx
        self.rockety = rockety
        self.velocity =velocity
        self.mass = rocketM
        self.angle = rocketA
    def draw(self,screen,size):
        pygame.draw.circle(screen,(0,100,0),(self.rocketx,self.rockety),size)