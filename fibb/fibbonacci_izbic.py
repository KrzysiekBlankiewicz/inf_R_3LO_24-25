import pygame
import math
pygame.init()

def fibbonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

screen_width = 1000
screen_height = 1000
screen_center = (screen_width/4, screen_height/4)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Golden Spiral")
scale = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

running = True

fibbonacci_list = []
for i in range(6):
    fibbonacci_list.append(fibbonacci(i))
spiral_count = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    
    x, y = screen_center

    for i in range(len(fibbonacci_list) - 1, -1, -1):
        if spiral_count == 1:
           pygame.draw.arc(screen, (BLACK), ((x, y), (fibbonacci_list[i] * scale, fibbonacci_list[i] * scale)), math.pi / 2, math.pi)
           x = x + ((fibbonacci_list[i] * scale) / 2) - ((scale * fibbonacci_list[i - 1]) / 2)
        if spiral_count == 2:
            pygame.draw.arc(screen, (BLACK), ((x, y), (fibbonacci_list[i] * scale, fibbonacci_list[i] * scale)), 2 * math.pi, math.pi / 2)
            y += scale * fibbonacci_list[i] / 2 - (scale * (fibbonacci_list[i - 1]) / 2)
            x = x + fibbonacci_list[i] * scale - (scale * (fibbonacci_list[i - 1]))
        if spiral_count == 3:
            pygame.draw.arc(screen, (BLACK), ((x, y), (fibbonacci_list[i] * scale, fibbonacci_list[i] * scale)), (3 / 2) * math.pi, 2 * math.pi)
            x = x + ((scale * fibbonacci_list[i]) / 2) - (scale * (fibbonacci_list[i - 1] / 2))
            y = y + (scale * fibbonacci_list[i]) - (scale * (fibbonacci_list[i - 1]))
        if spiral_count == 4:
            pygame.draw.arc(screen, (BLACK), ((x, y), (fibbonacci_list[i] * scale, fibbonacci_list[i] * scale)), math.pi, (3 / 2) * math.pi)
            y = y + scale * fibbonacci_list[i] / 2 - (scale * (fibbonacci_list[i - 1]) / 2)
        if spiral_count == 4:
            spiral_count = 1
        else:
            spiral_count += 1


    pygame.display.flip()
    
pygame.quit()
