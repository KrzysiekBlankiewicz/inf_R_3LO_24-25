import pygame

class Pion:
    def __init__(self, hex):
        self.hex = hex
    def draw(self, screen,size):
        pygame.draw.circle(screen,(200,0,0),(self.hex.xPos,self.hex.yPos),size)
    def move(self, gdziedzbanie):
        self.hex = gdziedzbanie
    