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
    def __init__(R, xp, yp, mp, cp, rp, kr, vx, vy):
        super().__init__(xp,yp,mp, cp, rp)
        R.k=kr
        R.vy=vx
        R.vx=vy

    def przyspiesz(R, v):
        r.v+=sila(r, p1)+sila(r, p2)+sila(r, p3)/R.m
        
def distance(rak, plan):
    d= math.sqrt((rak.x-plan.x)**2+(rak.y-plan.y)**2)
    return d

def sila(rak, plan):
    F= G*rak.m*plan.m/distance(rak, plan)**2
    return F
#
##
###
####
#####
######
#zacznij śmietnik
def silax(rak, plan):
    F= G*rak.m*plan.m/(plan.x-rak.x)**2
    return F

def silay(rak, plan):
    F= G*rak.m*plan.m/(plan.y-rak.y)**2
    return F
#kończ śmietnik
######
#####
####
###
##
#

def dajwektorsily(rak, plan):
    dx=(plan.x-rak.x)*sila(rak, plan)*100000
    dy=(plan.y-rak.y)*sila(rak, plan)*100000
    return (rak.x+dx, rak.y+dy)

def dajx(rak, plan):
    return((plan.x-rak.x)*sila(rak, plan)*100000)
def dajy(rak, plan):
    return((plan.y-rak.y)*sila(rak, plan)*100000)


def rysujwektorsily(screen, rak , plan):
    pygame.draw.line(screen, (0,250,0), (rak.x, rak.y),(dajwektorsily(rak, plan)), 3 )


def sila_wypadkowa(r, p1,p2,p3):
    siław= sila(r, p1)+sila(r, p2)+sila(r, p3)
    Wx=dajx(r, p1)+dajx(r, p2)+dajx(r, p3)
    Wy=dajy(r, p1)+dajy(r, p2)+dajy(r, p3)
   
    print((r.x+Wx, r.y+Wy))
    return (r.x+Wx, r.y+Wy)

def wypx(r, p1,p2,p3):
    return (dajx(r, p1)+dajx(r, p2)+dajx(r, p3))
            
def wypy(r, p1,p2,p3):
    return (dajy(r, p1)+dajy(r, p2)+dajy(r, p3))


Plenty=[]
mars=Planeta(xPlanety1,yPlanety1,masaPlanety1, (250, 150, 25), 25)
jowisz=Planeta(xPlanety2,yPlanety2,masaPlanety2, (23, 150, 250), 50)
wenus=Planeta(xPlanety3,yPlanety3,masaPlanety3, (200, 200, 50), 10)
rakieta=Rakieta(xRakiety,yRakiety,masaRakiety, (250, 10, 10),5, kątRakiety, prędkośćRakiety,0 )
Plenty.append(mars)
Plenty.append(jowisz)
Plenty.append(wenus)

#screen.fill((0,0,20))
clock = pygame.time.Clock()
#print(silay(rakieta, mars))
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((0,0,20))
    
    for x in Plenty:
        rysujwektorsily(screen, rakieta, x)
        
        x.rysuj_planetę(screen)

    pygame.draw.line(screen, (250,0,0), (rakieta.x, rakieta.y),(sila_wypadkowa(rakieta, mars, jowisz, wenus)), 5 )
    
    rakieta.rysuj_planetę(screen)

    print(wypx(rakieta, mars, jowisz, wenus))
    print(wypy(rakieta, mars, jowisz, wenus))
    rakieta.vx+=wypx(rakieta, mars, jowisz, wenus)/(rakieta.m*1)
    rakieta.vy+=wypy(rakieta, mars, jowisz, wenus)/(rakieta.m*1)
    rakieta.x+=rakieta.vx
    rakieta.y+=rakieta.vy
    print(rakieta.x)
    print(rakieta.y)
    
    pygame.display.flip()

pygame.quit()
