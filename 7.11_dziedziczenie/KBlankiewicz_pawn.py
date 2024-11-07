import pygame
import random

blue = (0, 0, 255)
white = (255, 255, 255)

class Pawn:
    def __init__(self, hex, key1, key2):
        self.hex = hex
        self.move_key = key1
        self.action_key = key2
        self.dead = False
        
    def move(self, destHex):
        if self.hex.isNeighbour(destHex):
            self.hex.occupied = False
            self.hex = destHex
            destHex.addPawn(self)
            
    def draw(self, a_prime, middle, screen, r):
        position = self.hex.pawnPosition(a_prime, middle)
        if self.dead:
            pygame.draw.circle(screen, white, position, r)
        else:
            pygame.draw.circle(screen, blue, position, r)

    def move_management(self, key):
        if self.dead:
            return
        if key == self.move_key:
            destination = random.choice(self.hex.neighbours)
            self.move(destination)
            
    def action_management(self, key):
        pass
    
class Warrior(Pawn):
    def action_management(self, key):
        if key == self.action_key:
            for n in self.hex.neighbours:
                if n.occupied:
                    n.pawn.dead == True
                    n.occupied = False
                       




    
