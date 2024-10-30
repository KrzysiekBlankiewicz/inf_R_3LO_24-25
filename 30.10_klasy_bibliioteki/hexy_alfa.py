#by Jozek
import math
import pygame

White = (255, 255, 255)
Green = (0, 255, 0)
Black = (0, 0, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)
kolor_hex = Red

Ile_Hex_y = 25
ile_hex_x = 25
offset = 2
a = 50
a_prime = a + offset / math.sqrt(3)
q = 0
r = 0
s = 0
num_sides = 6


class Hex:
    adjacent = []
    def __init__ (self, q, r, s):
        self.q = q
        self.s = s
        self.r = r
    def addAdjacent(self, otherHex):
        adjacent.append(otherHex)

    def draw(self, j, size, screen):
        hexCenter5 = hex_up(self.q, self.r, self.s, a_prime, j, size)
        hexCenter6 = hex_down(self.q, self.r, self.s, a_prime, j, size)
        angle = 2 * math.pi / num_sides
        points6 = []
        points5 = []
        for i in range(num_sides):
            x1 = hexCenter5[0] + a * math.cos(angle * i)
            y1 = hexCenter5[1] + a * math.sin(angle * i)
            x = hexCenter6[0] + a * math.cos(angle * i)
            y = hexCenter6[1] + a * math.sin(angle * i)
            points5.append((x1, y1))
            points6.append((x, y))
        if self.q == 0 and self.r ==0 and self.s ==0:
            pygame.draw.polygon(screen, Blue, points6)
            pygame.draw.polygon(screen, Blue, points5) 
        else:
            pygame.draw.polygon(screen, kolor_hex, points6)
            pygame.draw.polygon(screen, kolor_hex, points5)

    
def hex_up(q, r, s, a, j, size):
    if q + r + s != 0:
        return False
    xHexCenter = q * (3 / 2) * a + size[0] / 2
    yHexCenter = ((s + j) - (r - j)) * (a * math.sqrt(3)) / 2 + size[1] / 2
    return (xHexCenter, yHexCenter)

def hex_down(q, r, s, a, j, size):
    if q + r + s != 0:
        return False
    xHexCenter = q * (3 / 2) * a + size[0] / 2
    yHexCenter = ((s - j) - (r + j)) * (a * math.sqrt(3)) / 2 + size[1] / 2
    return (xHexCenter, yHexCenter)



