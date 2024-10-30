import pygame
 
pygame.init()
 
a = 100
offset = 5
radius = 10
 
screen = pygame.display.set_mode([a * radius + offset, a * radius + offset])
 
X = (a + offset) / 2
Y = (a + offset) / 2
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    screen.fill((0, 0, 0))  
 
    for x in range(radius):
        for y in range(radius):
            pygame.draw.rect(screen, (150, 0, 255), pygame.Rect(x*a+offset, y*a+offset, a-offset, a-offset))

 
 
    
    ruch = input("twój ruch: ")
 
 
    
    Cpos = (X, Y)
 
    if ruch == "w" and Y-a > 0 :
        Y=Y-a
        Cpos = (X, Y)
    elif ruch == "a" and X-a > 0:
        X=X-a
        Cpos = (X, Y)
    elif ruch == "s" and Y+a < a * radius + offset:
        Y=Y+a
        Cpos = (X, Y)  
    elif ruch == "d" and X+a < a * radius + offset:
        X=X+a
        Cpos = (X, Y)  
    else:
        Cpos = Cpos
    Kolo = pygame.draw.circle(screen, (255, 255, 255), Cpos, (a - offset) / 2)
 
    
 
    pygame.display.flip()  
 
pygame.quit()
