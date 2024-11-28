import objects as o
import drawer as d
import pygame

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
objects = []

class Simulator:
    def __init__(self, dataFileName):
        f = open(dataFileName, "r").readlines()
        self.rocket = o.Rocket(int(f[0]), int(f[1]), int(f[2]), blue)
        self.planets = []
        for i in range(3, len(f), 3):
            newPlanet = o.Planet(int(f[i]), int(f[i+1]), int(f[i+2]), red)
            self.planets.append(newPlanet)
    def gravityVector(self, obj1, obj2):
        force = obj1.gravityForce(obj2)
        x = (obj2.x - obj1.x)*force/500
        y = (obj2.y - obj1.y)*force/500
        return(x, y)

    def x(self, target, agent):
        vector = self.gravityVector(target, agent)
        start = (target.x, target.y)
        end = (start[0]+vector[0], start[1] + vector[1])
        d.drawLine(start, end, green)
    
    def showForces(self):
        for i in self.planets:
            self.x(self.rocket, i)

    def run(self):
        d.init()
        running = True
        while running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
            s.rocket.draw()
            for i in s.planets:
                i.draw()
            s.showForces()

            d.flip()
            
        pygame.quit()
    
s = Simulator("data.txt")
s.run()


