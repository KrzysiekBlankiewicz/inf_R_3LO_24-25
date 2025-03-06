import math
import pygame
import funkcjedogry
import time

class Node:
    def __init__(self, ID ,cords):
        self.ID = ID
        self.cords = cords
        self.neighbour = []  

    def addneighbour(self, neighbour):
        self.neighbour.extend(neighbour)

pygame.init()

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
            for neighbour in node.neighbours:
                if neighbour not in visited:
                    steps.append(path + [neighbour])  

        id += 1
        screen.fill((0, 0, 0))
        for n in nodes:
            if n in visited:
                n.draw(a, A, middle, screen, (200, 200, 200))  
            else:
                n.draw(a, A, middle, screen)

        pygame.display.flip()
        time.sleep(0.1)  

    return False 

a = 30
offset = 5
A = a + offset / math.sqrt(3)
screenY = 500
screenX = 500
radius = 3
middle = (screenX/2, screenY/2)
screen = pygame.display.set_mode([screenX, screenY])

nodes = []
k = 0
for q in range(-radius, radius + 1):
    for r in range(-radius, radius + 1):
        s = -q - r
        if abs(q) + abs(r) + abs(s) <= radius * 2:
            hex1 = funkcjedogry.Hex(q, -q-s, s)
            hex1.ID = k
            nodes.append(hex1)
            k += 1

funkcjedogry.setNeighbourhood(nodes)

start = nodes[1]  
destination = nodes[32]  
path = bfs(start, destination)

if path:
    for node in path:
        screen.fill((255, 255, 255))
        for n in nodes:
            if n in path:
                n.draw(a, A, middle, screen, (0, 255, 0))  
            else:
                n.draw(a, A, middle, screen)

        pygame.display.flip()
        time.sleep(0.3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for node in nodes:
        node.draw(a, A, middle, screen)  

    pygame.display.flip()

pygame.quit()
