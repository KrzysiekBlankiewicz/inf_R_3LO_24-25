import pygame
from pygame import Color

pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode([600, 600])
x = 17
#int(input("Ile kwadratow x"))
y =17
#int(input("ile kwadratow y"))
a =30
#int(input("wysokosc"))
b =30
#int(input("szerokosc"))
offset = 4
#int(input("offset"))
blue = Color(0,0, 255)
red = (255,0,0)
black = (0,0,0)

def kwadracikx(x, a, offset):
    xcord = a * x + offset * x + 0.5 * a

    return xcord
def kwadraciky(y, b, offset):

    ycord = b * y + offset * y + 0.5 * b
    return ycord

P = 1

xSize = x
ySize = y
circleX = 30
circleY = 30
# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    for j in range(0, ySize):
        for i in range(0, xSize):
            pozycjaPolaY= kwadraciky(j, a, offset)
            pozycjaPolaX = kwadracikx(i,b, offset)
            pygame.draw.rect(screen, black, (int((pozycjaPolaX)), int((pozycjaPolaY)), a, b))

    pygame.draw.circle(screen, red, (circleX, circleY),12)
    pygame.display.flip()


    move = input("rusz sie")
    
    if move == "d":
       circleX = circleX+34
       if circleX > 600:
           print("wyszedles za plansze lol")
           running = False
       
    elif move == "a":
       circleX = circleX-34
       if circleX < 30:
           print("wyszedles za plansze lol")
           running = False
    elif move == "s":
       circleY = circleY+34
       if circleY > 600:
           print("wyszedles za plansze lol")
           running = False
    
    elif move == "w":
       circleY = circleY-34
       if circleY < 30:
           print("wyszedles za plansze lol")
           running = False
       
    else:
        print("stary dziadzie graj w ta gre dobrze")
        running = False
        

pygame.quit()
   ### pygame.draw.circle(screen, red, (30 + 34*right - 34*left,30 + 34*down - 34*up),12)
    



    
    
        
        
    
    
