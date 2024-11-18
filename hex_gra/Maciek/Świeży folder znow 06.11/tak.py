import math
import pygame
import hexagon
import pionek 
pygame.init()
 
xrozmiar=1000
yrozmiar=1000
a=25
offset=3
xcenter=xrozmiar/2
ycenter=yrozmiar/2
screen = pygame.display.set_mode((xrozmiar, yrozmiar))
BLINK = (20, 160, 190)
NIC=(0,0,0)
BLUE = (32, 178, 170)
RED=(250, 50, 100)
HexLista=[]



radius = 10
for q in range(0, radius+1):
    for r in range(-radius, radius+1-q):
        hexa=hexagon.Hexagon(q,r,-q-r,NIC)
        HexLista.append(hexa)

for q in range(-radius, 0):
    for s in range(radius, -radius-q-1,-1):
        hexa=hexagon.Hexagon(q,-q-s,s,NIC)
        HexLista.append(hexa)

hexagon.daj_im_siadow(HexLista)

for x in HexLista:
    siedzi=x.siedzi
    
r1=pionek.ruszator((pygame.K_q,pygame.K_w,pygame.K_e,pygame.K_a,pygame.K_s,pygame.K_d))        
pion=pionek.pionek(HexLista[0],NIC, r1,BLUE,'b')

r2=pionek.ruszator((pygame.K_u,pygame.K_i,pygame.K_o,pygame.K_j,pygame.K_k,pygame.K_l))
pion2=pionek.pionek(HexLista[2*radius],NIC, r2,RED,'r')

#pion2=pionek.pionek(HexLista[8])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pion.kontrol_ruch(event)
            pion2.kontrol_ruch(event)

    screen.fill(BLINK)
    
    for h in HexLista:
        h.rysuj_hex(xcenter,ycenter,a, offset, screen, h.kolor)
        
    pion.rysuj_piona(screen,a, xcenter, ycenter)
    pion2.rysuj_piona(screen,a, xcenter, ycenter)
    pygame.display.flip()

pygame.quit()

 
 



