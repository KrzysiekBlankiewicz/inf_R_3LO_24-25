import math
import pygame
import hexagon
import pionek
import random
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



visited=[]
def dfs(start, meta):
    print(start)
    global visited
    if start==meta:
        return [start]
    visited.append(start)
    for s in start.siedzi:
        if s not in visited:
            tymc=dfs(s, meta)
            if  tymc!=False:
                return [start]+ tymc
    return False

visiteb=[]
def bfs(start, meta):
    print(start.id)
    global visiteb
    visiteb.append(start)
    id=0
    while visiteb[id]!=meta:
        a=visiteb[id]
        for s in a.siedzi:
            if s not in visiteb:
                visiteb.append(s)
        id+=1
        if id>len(visiteb)-1:
            return False
    return "wiwat"




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
    
start=random.choice(HexLista)
meta=random.choice(HexLista)
deefesy=[(dfs(start,meta))]

    


#pion2=pionek.pionek(HexLista[8])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BLINK)
    
    for h in HexLista:
        if h in visited:
            h.zajmij(1,(50,250,30))
        if h in deefesy:
            h.zajmij(1,(0,0,230))
            
        if h == start:
            h.zajmij(1,RED)
        if h == meta:
            h.zajmij(1,(0,200,0))
        
        
        h.rysuj_hex(xcenter,ycenter,a, offset, screen, h.kolor)
        
    pygame.display.flip()

pygame.quit()

