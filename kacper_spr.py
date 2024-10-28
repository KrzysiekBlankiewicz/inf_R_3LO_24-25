

xSize= 12
ySize = 12
a = 30
offset = 3

kol = 0
kol = 0
userx= 0
usery= 0 

def kwadracik(x,y):
    
    xcord = a*x + offset*x +0.5*a
    ycord = a*y + offset*y +0.5*a
    return xcord,ycord

def kolko(x,y):
    xcord = a*x + offset*x+a
    ycord = a*y + offset*y+a
    return xcord,ycord
# Import and initialize the pygame library
import pygame
pygame.init()
 
# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
 
# Run until the user asks to quit
running = True
while running:
 

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # Fill the background with white
    screen.fill((255, 255, 255))
 
    for x in range(0,xSize):
        for y in range(0,ySize):  
            v = kwadracik(x,y)
            pygame.draw.rect(screen, (0,0,255),(v[0]-(a/2),v[1]-(a/2),a,a))
    kolo = kolko(userx,usery)
    pygame.draw.circle(screen,(0,255,0),(kolo[0]-(a/2),kolo[1]-(a/2)),a/3)
    print(x)
    print(y)

    # Flip the display
    pygame.display.flip()
    user = input()
    if user == "w":
        usery = usery-1
    if user == "s":
        usery = usery +1
    if user =="a":
        userx = userx -1
    if user == "d":
        userx = userx +1
        
    print(user)
# Done! Time to quit.
pygame.quit()