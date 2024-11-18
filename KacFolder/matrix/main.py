import pygame
import math
sizeX =1000
sizeY = 1000

screen = pygame.display.set_mode([sizeX, sizeY])
pygame.init()

class Rocket:
    def __init__(self,rocketx,rockety,velocity,mass,angle):
        self.rocketx = rocketx
        self.rockety = rockety
        self.velocity =velocity
        self.mass = mass
        self.angle = angle
    def draw(self,screen,size):
        pygame.draw.circle(screen,(200,0,0),(self.rocketx,self.rockety),size)
        
class Planet:
    def __init__(self,planetx,planety,mass) :
        self.planetx = planetx
        self.planety = planety
        self.mass = mass
    def draw(self):
        pass

running = True

while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rakietka = Rocket(500,100,100,5,5)
    rakietka.draw(screen,50)
    pygame.display.flip()

pygame.quit()