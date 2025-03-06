import math
import pygame
import GRAHEXY

pygame.init()

def vertices(position, l):
    x = position[0]
    y = position[1]
    v1 = (x - l/2, y + (l * math.sqrt(3))/2 )
    v2 = (x + l/2, y + (l * math.sqrt(3))/2 )
    v3 = (x + l, y)
    v4 = (x + l/2, y - (l * math.sqrt(3))/2 )
    v5 = (x - l/2, y - (l * math.sqrt(3))/2 )
    v6 = (x - l, y)
    return [v1, v2, v3, v4, v5, v6]

class Node:
    def __init__(self, ID ,cords):
        self.ID = ID
        self.cords = cords
        self.neighbour = []

    def addneighbour(self, neighbour):
        self.neighbour.extend(neighbour)

color = (150, 0, 200)
l = 30
offset = 5
A = l + offset / math.sqrt(3)
screenY = 1000
screenX = 1000
radius = 3
middle = (screenX / 2, screenY / 2)
screen = pygame.display.set_mode([screenX, screenY])

a = Node("a", (500, 100))
b = Node("b", (800, 300))
c = Node("c", (500, 800))
d = Node("d", (200, 300))
e = Node("e", (800, 700))
f = Node("f", (500, 500))
g = Node("g", (500, 200))

nodes = [a, b, c, d, e, f]

a.addneighbour([d, f, b])
b.addneighbour([e, a])
c.addneighbour([e])
d.addneighbour([a])
e.addneighbour([b, c])
f.addneighbour([a])

def bfs(start, destination):
    steps = [[start]]  
    id = 0
    visited = []  

    while id < len(steps):
        path = steps[id]  
        node = path[-1]  

        if node == destination:
            return path  

        if node not in visited:
            visited.append(node)  
            for neighbour in node.neighbour:
                if neighbour not in visited:
                    steps.append(path + [neighbour])  

        id += 1

    return False 

steps = bfs(d, f)
print("steps:")
if steps == False:
    print("Can't do it")
else:
    for node in steps:
        print(node.ID)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 255, 255))


    for node in nodes:
        v = vertices(node.cords, l)
        pygame.draw.polygon(screen, color, v)


    pygame.display.flip()

pygame.quit()
