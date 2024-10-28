# Simple pygame program

def kwdx(x,a,offset):
    xcord = int(a*x + offset*x)
    return xcord
    
        
import pygame
pygame.init()
 
# Set up the drawing window
xysize=1000
screen = pygame.display.set_mode([xysize, xysize])
n=20
offset=1
a=int(1000/(n+1))
ycp=a/2
xcp=a/2
r=a+offset
running = True
while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False

     
    # Fill the background with white
    screen.fill((255, 255, 255))
    black=(0,0,0)
    color=(50, 20, 150)

    for x in range(n):
        for y in range(n):
            xpos=int(a*x+offset*x)
            ypos=int(a*y+offset*y)
            pygame.draw.rect(screen, black, (xpos, ypos, a, a))
    
    pygame.draw.circle(screen, color,(xcp,ycp),a/2)

    # Flip the display
    pygame.display.flip()

    ruh=input()
    if ruh== "a":
        xcp+= -r
    elif ruh=="w":
        ycp+=-r
    elif ruh=="s":
        ycp+= r
    elif ruh=='d':
        xcp+=r
    if xcp>xysize or xcp<0 or ycp>xysize or ycp<0:
        xcp= n/2*r+a/2
        ycp=n/2*r+a/2
 
# Done! Time to quit.
pygame.quit()
