import pygame
import math
pygame.init()

def fibbonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

def draw_goldenspiral(n):
    pygame.draw.arc(screen, BLACK, ((fibbonacci(n), fibbonacci(n)), (fibbonacci(n), fibbonacci(n))), 0, math.pi, 3)

screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Golden Spiral")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    draw_goldenspiral(10)
    pygame.display.flip()
    
pygame.quit()