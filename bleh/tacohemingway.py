import pygame


posxs = 500
posys = 500 
listaax = [500]
listaay = [500]


def methonone(x,y):
    nx =  -0.4*x-1
    ny = -0.4*y+0.1
    wyjscie = []
    wyjscie.append(nx)
    wyjscie.append(ny)
    return wyjscie

def methontwo(x,y):
    nx =  0.76*x - 0.4*y
    ny = 0.4*x + 0.76*y
    wyjscie = []
    wyjscie.append(nx)
    wyjscie.append(ny)
    return wyjscie

for i in range(1,10000000):
    posxs = methonone(posxs,posys)[0]
    posys = methonone(posxs,posys)[1]
    listaax.append(posxs)
    listaay.append(posys)




pygame.init()
screen = pygame.display.set_mode([1000, 1000])
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
    screen.fill((0, 0, 0))
    for i in range(0,len(listaax)):
        pygame.draw.line(screen,(0,255,0),(listaax[i],listaay[i]),(listaax[i],listaay[i]))
        
    pygame.display.flip()



pygame.quit()