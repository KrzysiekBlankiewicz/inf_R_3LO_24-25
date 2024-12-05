import pygame
import math
import random
class Rocket:
    def __init__(self,rocketx,rockety,velocityx,velocityy,rocketM):
        self.rocketx = rocketx
        self.rockety = rockety
        self.velocityx = velocityx
        self.velocityy = velocityy
        self.mass = rocketM
    def draw(self,screen,size):
        pygame.draw.circle(screen,(0,100,0),(self.rocketx,self.rockety),size)
