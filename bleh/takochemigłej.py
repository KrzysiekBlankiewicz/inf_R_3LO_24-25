import pygame
import random
import math
def method1(x,y):
    x_p = -0.4*x-1
    y_p = -0.4*y+0.1
    return [x_p,y_p]
def method2(x,y):
    x_p = 0.76*x-0.4*y
    y_p = 0.4*x+0.76*y
    return [x_p,y_p]

screen = pygame.display.set_mode([1000, 1000])
x =1
y= 1
lista= []
for x in range(1,1000000):
        opcja = random.randint(1, 2)
        if opcja == 1:
            x = method1(x,y)[0]
            y = method1(x,y)[1]
        if opcja == 2:
            x = method2(x,y)[0]
            y = method2(x,y)[1]
        lista.append([math.ceil(x),math.ceil(y)])
#print(lista)
running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    for x in lista:
        pygame.draw.line(screen, (0, 0, 0), 
                         [x[0], x[1]], 
                         [x[0], x[1]], 1)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()