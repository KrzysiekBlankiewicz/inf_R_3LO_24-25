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
nieaktywne=[]


visited=[]
def dfs(start, meta):
#    print(start)
    global visited
    global nieaktywne
    if start==meta:
        return [start]
    visited.append(start)
    for s in start.siedzi:
        if s not in visited:
            if s not in nieaktywne:
                tymc=dfs(s, meta)
                if  tymc!=False:
                    return [start]+ tymc
    return False

visiteb=[]
def bfs(start, meta):
#   print(start.id)

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
        hexa=hexagon.Hexagon(q,r,-q-r,(250,128,114))
        HexLista.append(hexa)

for q in range(-radius, 0):
    for s in range(radius, -radius-q-1,-1):
        hexa=hexagon.Hexagon(q,-q-s,s,(250,128,114))
        HexLista.append(hexa)

hexagon.daj_im_siadow(HexLista)

for x in HexLista:
    siedzi=x.siedzi


for i in range(30):
    x=random.randint(1,300)
    nieaktywne.append(HexLista[x+1])
    nieaktywne.append(HexLista[x+2])
    nieaktywne.append(HexLista[x+3])
    nieaktywne.append(HexLista[x+4])
    nieaktywne.append(HexLista[x+10])        


start=random.choice(HexLista)
meta=random.choice(HexLista)

while start in nieaktywne:
    start=random.choice(HexLista)
while meta in nieaktywne:
    meta=random.choice(HexLista)


deefesy=dfs(start,meta)
if deefesy != False:
    print(len(deefesy))



#for i in range(len(deefesy)):
#    deefesy[i]=hexagon.Hexagon(deefesy[i])

#print(nieaktywne)   
if deefesy in HexLista:
    print(hura)

#pion2=pionek.pionek(HexLista[8])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BLINK)
    
    for i in range (len(HexLista)):
        h=HexLista[i]
        if h in nieaktywne:
            h.zajmij(1,(0,0,0))
        if h in visited:
            h.zajmij(1,(50,250,30))
        if deefesy!= False and h in deefesy:
            x=deefesy.index(h)
            y=250//len(deefesy)
            h.zajmij(1,(x*y,50,x*y))
            
        if h == start:
            h.zajmij(1,RED)
        if h == meta:
            h.zajmij(1,(0,200,0))
        
        h.rysuj_hex(xcenter,ycenter,a, offset, screen, h.kolor)
        
    pygame.display.flip()

pygame.quit()

