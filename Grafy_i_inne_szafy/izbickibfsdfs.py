import math
import pygame


visited = []
a = 30
offset = 5
A = a + offset / math.sqrt(3)
screenY = 500
screenX = 500
radius = 3
middle = (screenX/2, screenY/2)
screen = pygame.display.set_mode([screenX, screenY])
listahexy = []
color = (0, 0, 0)

class Node:
    def __init__(self, id):
        self.id = id
    def add_soms(self, soms):
        self.soms = soms

def dfs(start, dest):
    global visited
    route = [start]
    if start == dest:
        return route
    visited.append(start)
    for s in start.soms:
        if s not in visited:
            temp = dfs(s,dest)
            if temp != False:
                return route + temp
    return False

def bfs(start, dest):
    steps = [start] 
    id = 0
    visited = []  
 
    while id < len(steps):
        path = steps[id]  
        node = path[-1]  
 
        if node == dest:
            return path  
 
        if node not in visited:
            visited.append(node)  
            for neighbour in node.neighbour:
                if neighbour not in visited:
                    steps.append(path + [neighbour])
 
 
def position(q, r, s, a):
    if q + r + s != 0:
        return False
    xPos = q * (1.5 * a)
    yPos = (s - r) * (a * math.sqrt(3) )/2
 
    return (xPos, yPos)
 
def topLeftPosition(hexPosFromCenter, screenCenter):
    xPos = hexPosFromCenter[0] + screenCenter[0]
    yPos = hexPosFromCenter[1] + screenCenter[1]
    return (xPos, yPos)
 
def vertices(position, a):
    x = position[0]
    y = position[1]
    v1 = (x - a/2, y + (a * math.sqrt(3))/2 )
    v2 = (x + a/2, y + (a * math.sqrt(3))/2 )
    v3 = (x + a, y)
    v4 = (x + a/2, y - (a * math.sqrt(3))/2 )
    v5 = (x - a/2, y - (a * math.sqrt(3))/2 )
    v6 = (x - a, y)
    return [v1, v2, v3, v4, v5, v6]

class Hex:
    def __init__(self, q, r, s):
        self.q = q
        self.r = r
        self.s = s
        self.neighbours = []
    def addNeighbour(self, innyhex):
        if innyhex not in self.neighbours:
            self.neighbours.append(innyhex)

 
 
    def draw(self, a, A, middle, screen):
        hexFromCenterPosition = position(self.q, self.r, self.s, A)
        properPosition = topLeftPosition(hexFromCenterPosition, middle)
        verticesList = vertices(properPosition, a)
        pygame.draw.polygon(screen, color, verticesList)
 
    def pawnPosition(self, A, middle):
        hexFromCenterPosition = position(self.q, self.r, self.s, A)
        properPosition = topLeftPosition(hexFromCenterPosition, middle)
        return properPosition
    def isNeighbour(self, innyhex):
        if self.q == innyhex.q and abs(self.r - innyhex.r) == 1 and abs(self.s - innyhex.s) == 1:
            return 1
        if self.r == innyhex.r and abs(self.q - innyhex.q) == 1 and abs(self.s - innyhex.s) == 1:
            return 1
        if self.s == innyhex.s and abs(self.r - innyhex.r) == 1 and abs(self.q - innyhex.q) == 1:
            return 1
        return 0
 
def setNeighbourhood(hexy):
    for a in hexy:
        for b in hexy:
            if a.isNeighbour(b) == 1:
                a.addNeighbour(b)
                b.addNeighbour(a)
 
for q in range(-radius, radius + 1):
        for r in range(-radius, radius + 1):
            s = -q - r
            if abs(q) + abs(r) + abs(s) <= radius * 2:
                hex1 = Hex(q, -q-s, s)
                listahexy.append(hex1)
 
setNeighbourhood(listahexy)

pygame.init()

for i in listahexy():
    pass
 
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for h in listahexy:
        h.draw(a, A, middle, screen)
    pygame.display.flip()
pygame.quit




route = dfs()
if route != False:
    print("route:")
    for i in range(len(route)):
        route[i] = route[i].id
        print(route[i])
else:
    print("Error 404: no route found!")