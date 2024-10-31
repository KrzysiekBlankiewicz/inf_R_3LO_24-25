import pygame
import random

blue = (0, 0, 255)

class Pawn:
    def __init__(self, hex):
        self.hex = hex

    def move(self, destHex):
        if self.hex.isNeighbour(destHex):
            self.hex = destHex
            
    def draw(self, a_prime, middle, screen, r):
        position = self.hex.pawnPosition(a_prime, middle)
        pygame.draw.circle(screen, blue, position, r)

    def randomMove(self):
        destination = random.choice(self.hex.neighbours)
        self.move(destination)
