import pygame
import sys
import random
import math

pygame.init()

# screen init
screen_width, screen_height = 800, 800
center = [screen_width / 2, screen_height / 2]
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sito Eratostenesa")

# square & circle data
square_size = 600
outline_width = 3


pygame.font.init()
font = pygame.font.SysFont('Arial', 24)

def sito_erastotenesa(count):
    inside = 0
    outside = 0
    for i in range(count):
        x = random.randint(-300, 300) + 400
        y = random.randint(-300, 300) + 400
        pygame.draw.circle(screen, (0, 255, 0), (x, y), 2)
        if (x - 400)**2 + (y - 400)**2 < 300**2:
            inside += 1
        else:
            outside += 1
    return inside / (inside + outside)

screen.fill((0, 0, 0))
pygame.draw.rect(screen, (255, 255, 255), (center[0] - square_size / 2, center[1] - square_size / 2, square_size, square_size), 4)
pygame.draw.circle(screen, (255, 255, 255), center, square_size // 2, 4)

ratio = sito_erastotenesa(10000)
pi_estimate = 4 * ratio
caption_text = f"przybliżenie π z użyciem metody Monte Carlo: π ≈ {pi_estimate:.5f}"
text_surface = font.render(caption_text, True, (255, 255, 255))
text_rect = text_surface.get_rect(center=(screen_width / 2, screen_height - 30))
screen.blit(text_surface, text_rect)

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
