import pygame
import random

color = (0, 0, 0)

class pawn:
    def __init__(self, hex):
        self.hex = hex

    def ruch(self, gdzieide):
        if self.hex.isNeighbour(gdzieide):
            self.hex = gdzieide
            
    def draw(self, A, middle, screen, p):
        position = self.hex.pawnPosition(A, middle)
        pygame.draw.circle(screen, color, position, p)

    def randomruch(self):
        gdzie = random.choice(self.hex.neighbours)
        self.ruch(gdzie)
    
   # def poladoruchu( self, hex):
   #     pole1 = 
    #    pole2 =
    #    pole3 =
     #   pole4 = 
      #  pole5 = 
       # pole6 = 
