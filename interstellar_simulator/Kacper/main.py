import pygame
import math
import random
from rocket import Rocket
from planet import Planet

sizeX, sizeY = 1000, 1000
screen = pygame.display.set_mode([sizeX, sizeY])
pygame.init()


planet_number = int(input("Podaj liczbe obiektow: "))

planet_size = 30
planet_list = []


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def gravity(m1, m2, x1, y1, x2, y2):
    g = 6.67 * 10**(-11)
    r = distance(x1, y1, x2, y2)
    return g * m1 * m2 / r**2

def vector(m1, m2, x1, y1, x2, y2):
    sila = gravity(m1, m2, x1, y1, x2, y2)
    fx = sila * (x2 - x1) *1000000000
    fy = sila * (y2 - y1) *1000000000
    return fx, fy

for x in range(planet_number):
    planet = Planet(random.randint(1, 1000), random.randint(1, 1000), 10000)
    planet_list.append(planet)

running = True
rakieta = Rocket(0, 0, 0,0, 100)

clock = pygame.time.Clock()

while running:
    clock.tick(60)
    wypx = 0
    wypy = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0)) 

    rakieta.draw(screen, 10)

    for planeta in planet_list:
        planeta.draw(screen, planet_size)
        fx, fy = vector(rakieta.mass, planeta.mass, rakieta.rocketx, rakieta.rockety, planeta.planetx, planeta.planety)
        wypx += fx
        wypy += fy
        pygame.draw.line(screen, (0, 255, 0), (rakieta.rocketx, rakieta.rockety), (rakieta.rocketx+fx, rakieta.rockety+fy), 5)
    print(wypx,wypy)
    ax= wypx/rakieta.mass
    ay = wypy/rakieta.mass
    rakieta.velocityx+=ax/100
    rakieta.velocityy+=ay/100
    rakieta.rocketx +=rakieta.velocityx
    rakieta.rockety +=rakieta.velocityy
    pygame.draw.line(screen, (0, 0, 200), (rakieta.rocketx, rakieta.rockety), (wypx+rakieta.rocketx, wypy+rakieta.rockety), 5)
    pygame.display.flip()

pygame.quit()
