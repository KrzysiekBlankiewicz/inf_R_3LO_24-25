Dane=open('dane.txt').read().splitlines()
import math
import pygame

pygame.init()
screen = pygame.display.set_mode((1000,1000))

for i in range(len(Dane)):
    Dane[i]=int(Dane[i])



xRakiety=Dane[0]
yRakiety=Dane[1]
masaRakiety=Dane[2]
kątRakiety=Dane[3]
prędkośćRakiety=Dane[4]

xPlanety1=Dane[5]
yPlanety1=Dane[6]
masaPlanety1=Dane[7]

xPlanety2=Dane[8]
yPlanety2=Dane[9]
masaPlanety2=Dane[10]

xPlanety3=Dane[11]
yPlanety3=Dane[12]
masaPlanety3=Dane[13]

G= 6.6743015152*10**(-11)

class Planeta:
    def __init__(P, xp, yp, mp, cp, rp):
        P.x=xp
        P.y=yp
        P.m=mp
        P.c=cp
        P.r=rp

    def rysuj_planetę(P,screen):
          pygame.draw.circle(screen,P.c, (P.x,P.y), P.r)


class Rakieta(Planeta):
    def __init__(R, xp, yp, mp, cp, rp, kr, vr):
        super().__init__(xp,yp,mp, cp, rp)
        R.k=kr
        R.v=vr
        
        
def distance(rak, plan):
    d= math.sqrt((rak.x-plan.x)**2+(rak.y-plan.y)**2)
    return d

def sila(rak, plan):
    F= G*rak.m*plan.m/distance(rak, plan)**2
    return F

#zacznij śmietnik
def silax(rak, plan):
    F= G*rak.m*plan.m/(plan.x-rak.x)**2
    return F

def silay(rak, plan):
    F= G*rak.m*plan.m/(plan.y-rak.y)**2
    return F
#kończ śmietnik

def dajwektorsily(rak, plan):
    dx=(plan.x-rak.x)*sila(rak, plan)*1000
    dy=(plan.y-rak.y)*sila(rak, plan)*1000
    return (rak.x+dx, rak.y+dy)

def rysujwektorsily(screen, rak , plan):
    pygame.draw.line(screen, (0,250,0), (rak.x, rak.y),(dajwektorsily(rak, plan)), 3 )

def sila_wypadkowa(r, p1,p2,p3):
    Fwx=silax(r, p1)+silax(r, p2)+silax(r, p3)
    Fwy=silay(r, p1)+silay(r, p2)+silay(r, p3)
    return (Fwx, Fwy)

Plenty=[]
mars=Planeta(xPlanety1,yPlanety1,masaPlanety1, (250, 150, 25), 25)
jowisz=Planeta(xPlanety2,yPlanety2,masaPlanety2, (23, 150, 250), 50)
wenus=Planeta(xPlanety3,yPlanety3,masaPlanety3, (200, 200, 50), 10)
rakieta=Rakieta(xRakiety,yRakiety,masaRakiety, (250, 10, 10),5, kątRakiety, prędkośćRakiety )
Plenty.append(mars)
Plenty.append(jowisz)
Plenty.append(wenus)

print(456)

#print(silay(rakieta, mars))
running = True
while running:
    
    screen.fill((0,0,20))
    
    for x in Plenty:
        rysujwektorsily(screen, rakieta, x)
        
        x.rysuj_planetę(screen)

    pygame.draw.line(screen, (250,0,0), (rakieta.x, rakieta.y),(sila_wypadkowa(rakieta, mars, jowisz, wenus)), 5 )
    
    rakieta.rysuj_planetę(screen)
    
    
    pygame.display.flip()

pygame.quit()
