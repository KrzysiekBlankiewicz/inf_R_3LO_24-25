import pygame
import random

color = (0, 0, 0)

class pawn:
    def __init__(self, hex):
        self.hex = hex

    def ruch(self, destHex):
        if self.hex.isNeighbour(destHex):
            self.hex = destHex
            
    def draw(self, A, middle, screen, r):
        position = self.hex.pawnPosition(A, middle)
        pygame.draw.circle(screen, color, position, r)

    def randomruch(self):
        destination = random.choice(self.hex.neighbours)
        self.ruch(destination)
