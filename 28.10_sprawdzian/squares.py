import pygame
pygame.init()

n=10
offset = 5
size = 50 
circleposx = size/2+offset/2
circleposy = size/2+offset/2
ifmovedw = 0
ifmoveda = 0
ifmovedd = 0
ifmoveds = 0
# Set up the drawing window
screen = pygame.display.set_mode([size*n+offset,size*n+offset])

# Run until the user asks to quit
running = True
while running:
    
    # exit on user request
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # setup
    screen.fill((255, 255, 255))
    for hori in range(n):
        for vert in range(n):
            pygame.draw.rect(screen,(0,0,0),pygame.Rect(hori*size+offset, vert*size+offset, size-offset, size-offset))
    pygame.draw.circle(screen,(255,255,255),(circleposx, circleposy), size/10)
    pygame.display.flip()
    userinput = 'a'
    circleposy += ifmovedw * (size + offset)
    circleposy += ifmoveds * (size + offset)
    circleposx += ifmoveda * (size + offset)
    circleposx += ifmovedd * (size + offset)
    ifmovedw = 0
    ifmoveds = 0
    ifmoveda = 0
    ifmovedd = 0
    userinput = input("move circle")
    if  userinput == 'w':
        for hori in range(n):
            for vert in range(n):
                pygame.draw.rect(screen,(0,0,0),pygame.Rect(hori*size+offset, vert*size+offset, size-offset, size-offset))
        pygame.draw.circle(screen,(255,255,255),(circleposx, circleposy), size/10)
        pygame.display.flip()
        ifmovedw = 1
    elif userinput == 's':
        for hori in range(n):
            for vert in range(n):
                pygame.draw.rect(screen,(0,0,0),pygame.Rect(hori*size+offset, vert*size+offset, size-offset, size-offset))
        pygame.draw.circle(screen,(255,255,255),(circleposx, circleposy), size/10)
        pygame.display.flip()
        ifmoveds = -1
    elif userinput == 'a':
        for hori in range(n):
            for vert in range(n):
                pygame.draw.rect(screen,(0,0,0),pygame.Rect(hori*size+offset, vert*size+offset, size-offset, size-offset))
        pygame.draw.circle(screen,(255,255,255),(circleposx, circleposy), size/10)
        pygame.display.flip()
        ifmoveda = -1
    elif userinput == 'd':
        print("acb")
        for hori in range(n):
            for vert in range(n):
                pygame.draw.rect(screen,(0,0,0),pygame.Rect(hori*size+offset, vert*size+offset, size-offset, size-offset))
        pygame.draw.circle(screen,(255,255,255),(circleposx, circleposy), size/10)
        pygame.display.flip()
        ifmovedd = 1
# Done! Time to quit.
pygame.quit()