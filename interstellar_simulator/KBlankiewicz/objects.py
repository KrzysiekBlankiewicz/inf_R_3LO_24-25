import math
import drawer
g = 10


class Object:
    def __init__(self, m, x, y, color):
        self.m = m
        self.x = x
        self.y = y
        self.color = color
        self.r = m/100
        
    def gravityForce(self, other):
        dist_2 = (self.x-other.x)**2 + (self.y-other.y)**2
        return g * self.m * other.m / dist_2

    def gravityVector(self, obj):
        force = self.gravityForce(obj)
        x = (obj.x - self.x)*force/100
        y = (obj.y - self.y)*force/100
        return(x, y)

    def draw(self):
        drawer.drawCircle(self.x, self.y, self.r, self.color)

    def valueFromComponents(self, x, y):
        return math.sqrt(x**2 + y**2)

class Planet(Object):
    def __init__(self, m, x, y, color):
        super().__init__(m, x, y, color)

    
class Rocket(Object):
    def __init__(self, m, x, y, color):
        super().__init__(m, x, y, color)
        self.velocity = 0
        self.vX = 0
        self.vY = 0
        self.accel = 0
        self.aX = 0
        self.aY = 0

    def move(self, interactingObjects):
        resultantX = 0
        resultantY = 0
        for agent in interactingObjects:
            vector = self.gravityVector(agent)
            resultantX += vector[0]
            resultantY += vector[1]
        self.accel = self.valueFromComponents(resultantX, resultantY) / self.m
        self.aX = resultantX*self.accel/1000
        self.aY = resultantY*self.accel/1000
        self.vX += self.aX
        self.vY += self.aY
        self.velocity = self.valueFromComponents(self.vX, self.vY)
        self.x += self.vX
        self.y += self.vY



