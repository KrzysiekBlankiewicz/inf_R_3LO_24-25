import objects as o
import drawer as d
import pygame

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
objects = []

class Simulator:
    def __init__(self, dataFileName):
        f = open(dataFileName, "r").readlines()
        self.rocket = o.Rocket(int(f[0]), int(f[1]), int(f[2]), blue)
        self.planets = []
        for i in range(3, len(f)-1, 3):
            newPlanet = o.Planet(int(f[i]), int(f[i+1]), int(f[i+2]), red)
            self.planets.append(newPlanet)
        self.target = self.planets[int(f[-1])]
            
    def gravityVector(self, obj1, obj2):
        force = obj1.gravityForce(obj2)
        x = (obj2.x - obj1.x)*force/100
        y = (obj2.y - obj1.y)*force/100
        return(x, y)

    def drawForce(self, target, agent):
        vector = self.gravityVector(target, agent)
        start = (target.x, target.y)
        end = (start[0]+vector[0], start[1] + vector[1])
        d.drawLine(start, end, green)
        return vector
    
    def showForces(self):
        resultantX = 0
        resultantY = 0
        for i in self.planets:
            v = self.drawForce(self.rocket, i)
            resultantX += v[0]
            resultantY += v[1]
        start = (self.rocket.x, self.rocket.y)
        end = (start[0] + resultantX, start[1] + resultantY)
        d.drawLine(start, end, white)

    def drawCosmos(self):
        d.clear()
        self.rocket.draw()
        for i in self.planets:
            i.draw()
        self.showForces()
        d.flip()

    def setInitialVel(self, vX, vY):
        self.rocket.setInitialVel(vX, vY)
            
    def run(self):
        d.init()

        clock = pygame.time.Clock()
        
        self.rocket.draw()
        for i in self.planets:
            i.draw()
        self.showForces()

        print(self.rocket)
        for x in self.planets:
            print(x)
        print(self)
        
        running = True
        while running:
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False

            self.rocket.move(self.planets)

            travelEnd = self.rocket.checkEnd(self.planets)
            if travelEnd != None:
                if travelEnd == self.target:
                    print("success")
                else:
                    print("tragic end")
                running = False
                
            self.drawCosmos()
            clock.tick(30)
            
        pygame.quit()
    
s = Simulator("data.txt")
s.setInitialVel(5, 5)
s.run()


