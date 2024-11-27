import pygame
import math
import random
from rocket import Rocket
from planet import Planet

sizeX, sizeY = 1000, 1000
screen = pygame.display.set_mode([sizeX, sizeY])
pygame.init()

planet_number = 4
planet_size = 30
planet_list = []

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def gravity(m1, m2, x1, y1, x2, y2):
    g = 6.67 * 10**(-11)
    r = distance(x1, y1, x2, y2)
    if r == 0:  
        return 0
    return g * m1 * m2 / r**2

def vector(m1, m2, x1, y1, x2, y2):
    sila = gravity(m1, m2, x1, y1, x2, y2)
    fx = sila * (x2 - x1) * 1000000000000
    fy = sila * (y2 - y1) * 1000000000000
    return fx, fy

for _ in range(planet_number):
    planet = Planet(random.randint(100, 900), random.randint(100, 900), 10)
    planet_list.append(planet)

running = True
rakieta = Rocket(500, 500, 100, 100, 100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0)) 

    rakieta.draw(screen, 10)

    for planeta in planet_list:
        planeta.draw(screen, planet_size)
        
        fx, fy = vector(rakieta.mass, planeta.mass, rakieta.rocketx, rakieta.rockety, planeta.planetx, planeta.planety)
    
    
        pygame.draw.line(screen, (0, 255, 0), (rakieta.rocketx, rakieta.rockety), (rakieta.rocketx + fx, rakieta.rockety + fy), 2)

    pygame.display.flip()

pygame.quit()
