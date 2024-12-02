import pygame
import math
import random

sizeX = 1000
sizeY = 1000

screen = pygame.display.set_mode([sizeX, sizeY])
pygame.init()

class Rocket:
    def __init__(self, rocketx, rockety, velocity, mass, angle):
        self.rocketx = rocketx
        self.rockety = rockety
        self.velocity = velocity
        self.mass = mass
        self.angle = angle
    
    def draw(self, screen, size):
        pygame.draw.circle(screen, (255, 255, 255), (self.rocketx, self.rockety), size)

rocket = Rocket(500, 100, 100, 5, 5)

class Planet:
    def __init__(self, planetx, planety, mass):
        self.planetx = planetx
        self.planety = planety
        self.mass = mass

    def draw(self, screen, size):
        pygame.draw.circle(screen, (255, 0, 0), (self.planetx, self.planety), size)
    
    def drawlines(self, screen, rocket):
        pygame.draw.line(screen, (255, 0, 0), (rocket.rocketx, rocket.rockety), (self.planetx, self.planety))

planet_count = int(input("number of planets: "))
planets = []
running = True
for i in range(planet_count+1):
    planets.append(Planet(random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 100)))

# Poprawiona funkcja kąta
def angle(deltax, deltay):
    if deltay > 0:
        return math.atan(deltay / deltax)
    elif deltay < 0:
        return -math.atan(deltay / deltax)
    return 0  # Obsługuje przypadek, gdy deltay == 0

def gravity(rocketmass, planetmass, rocketx, rockety, planetx, planety):
    G = 10
    r = math.sqrt((rocketx - planetx)**2 +(rockety - planety)**2)
    return G*(rocketmass * planetmass)/r**2
    


    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Wyczyść ekran przed rysowaniem na nim nowych obiektów
    listF = []
    for elem in planets:
        F = gravity(rocket.mass, elem.mass, rocket.rocketx, rocket.rockety, elem.planetx, elem.planety)
        
    # Rysowanie planet
    for i in range(1, 5):  # Indeksy od 1 do 4, bo planeta 0 może być głównym obiektem
        planets[i].draw(screen, planets[i].mass)
        planets[i].drawlines(screen, rocket)

    # Rysowanie rakiety
    rocket.draw(screen, 10)

    pygame.display.flip()

pygame.quit()
