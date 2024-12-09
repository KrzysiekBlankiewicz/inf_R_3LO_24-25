import math
import pygame
import hexagon
import pionek 
pygame.init()
 
xrozmiar=1000
yrozmiar=1000
a=80
offset=3
xcenter=xrozmiar/2
ycenter=yrozmiar/2
screen = pygame.display.set_mode((xrozmiar, yrozmiar))
WHITE = (20, 160, 190)
NIC=(0,0,0)
BLUE = (32, 178, 170)

HexLista=[]



radius = 3
for q in range(0, radius+1):
    for r in range(-radius, radius+1-q):
        hexa=hexagon.Hexagon(q,r,-q-r)
        HexLista.append(hexa)

for q in range(-radius, 0):
    for s in range(radius, -radius-q-1,-1):
        hexa=hexagon.Hexagon(q,-q-s,s)
        HexLista.append(hexa)

hexagon.daj_im_siadow(HexLista)

for x in HexLista:
    siedzi=x.siedzi
    print( 'x:', x.q, x.r, x.s, )
    for y in siedzi:
        print('y:', y.q, y.r, y.s )
        
pion=pionek.pionek(HexLista[0])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pion.kontrol_ruch(event)

    screen.fill(WHITE)
    
    
    for h in HexLista:
        h.rysuj_hex(xcenter,ycenter,a, offset, screen, BLUE)
    pion.rysuj_piona(screen, NIC,a, xcenter, ycenter)

    pygame.display.flip()
pygame.quit()

 
 



