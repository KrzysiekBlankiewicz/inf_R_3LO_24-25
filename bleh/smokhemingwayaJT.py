import pygame
import random


pygame.init()
size = 1000
screen = pygame.display.set_mode((size, size))
screen.fill((0, 0, 0))

n = 1000000
x, y = 0.0, 0.0
center = (size // 2, size // 2)
scale = 300

def mode1(x, y):
    X = x * (-0.4) - 1
    Y = y * (-0.4) + 0.1
    return X, Y

def mode2(x, y):
    X = x * 0.76 - y * 0.4 
    Y = x * 0.4 + y * 0.76
    return X, Y


def drawpoint(x, y):
    X = int(center[0] + x * scale)
    Y = int(center[1] - y * scale)
    screen.set_at((X, Y), (255, 0, 0))

for i in range(n):
    drawpoint(x, y)
    if random.random() < 0.5:
        x, y = mode1(x, y)
    else:
        x, y = mode2(x, y)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
