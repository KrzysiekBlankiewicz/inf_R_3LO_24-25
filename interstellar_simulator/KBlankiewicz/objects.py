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

    def draw(self):
        drawer.drawCircle(self.x, self.y, self.r, self.color)
        

class Planet(Object):
    def __init__(self, m, x, y, color):
        super().__init__(m, x, y, color)


    
class Rocket(Object):
    def __init__(self, m, x, y, color):
        super().__init__(m, x, y, color)
