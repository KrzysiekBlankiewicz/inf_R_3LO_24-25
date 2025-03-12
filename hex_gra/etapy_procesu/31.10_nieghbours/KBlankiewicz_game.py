import math
import pygame
import KBlankiewicz_hex as hex
import KBlankiewicz_pawn as pawn

pygame.init()

a = 50
offset = 10
a_prime = a + offset / math.sqrt(3)
screenHeight = 1000
screenWidth = 1000
boardRadius = 3
middle = (screenWidth/2, screenHeight/2)
screen = pygame.display.set_mode([screenWidth, screenHeight])
playerRadius = 20

hexList = []

for q in range(-boardRadius, 0):
    for s in range(boardRadius, -boardRadius-q-1, -1):
        hex1 = hex.Hex(q, -q-s, s)
        hexList.append(hex1)
for q in range(0, boardRadius+1):
    for r in range(-boardRadius, boardRadius-q+1):
        hex2 = hex.Hex(q, r, -q-r)
        hexList.append(hex2)

hex.setNeighbourgood(hexList)

player = pawn.Pawn(hexList[0])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.randomMove()

    screen.fill((255, 255, 255))

    for h in hexList:
        h.draw(a, a_prime, middle, screen)

    player.draw(a_prime, middle, screen, playerRadius)
    
    pygame.display.flip()
    
pygame.quit()

