import objects as o
import pygame

red = (255, 0, 0)
blue = (0, 0, 255)
objects = []

class Simulator:
    def __init__(self, dataFileName)
        f = open(dataFileName, "r")
        rocketX = int(f[0])
        rocketY = int(f[1])
        rocketM = int(f[2])
        
        


p1 = o.Planet(1000, 100, 100, red)
objects.append(p1)
r = o.Rocket(500, 500, 500, blue)
objects.append(r)

for i in objects:
    i.draw()
    
pygame.display.flip()
