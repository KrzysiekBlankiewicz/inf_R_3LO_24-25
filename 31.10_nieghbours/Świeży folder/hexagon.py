#biblioteki
import math
import pygame


#funkcje

def srodek(xcenter, ycenter, q,r,s,a):
    if q+r+s==0:
        x=xcenter+q*(3/2)*a
        y=ycenter+s*a*math.sqrt(3)/2+(-r)*a*math.sqrt(3)/2
        return (x,y,a)



def wierzch(x, y, a):
    x1=x-a/2
    x2=x+a/2
    x3=x+a
    x4=x+a/2
    x5=x-a/2
    x6=x-a
    y1=y+a*math.sqrt(3)/2
    y2=y+a*math.sqrt(3)/2
    y3=y
    y4=y-a*math.sqrt(3)/2
    y5=y-a*math.sqrt(3)/2
    y6=y

    return (x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)


def rysuj(xcenter,ycenter,q,r,s,a, offset, screen, color):
    abc=srodek(xcenter,ycenter,q,r,s,a)
    defg=wierzch(abc[0],abc[1],abc[2]-offset)
    hexa_points=[]
    for x in range (0,11,2):
        gupio=[]
        gupio.append(defg[x])
        gupio.append(defg[x+1])
        hexa_points.append(gupio)
    pygame.draw.polygon(screen, color, hexa_points)


#klasa

class Hexagon:

    

    def __init__ (h, q, r, s):
        h.q=q
        h.r=r
        h.s=s
        h.siedzi=[]
    def rysuj_hex(h,xcenter,ycenter,a, offset, screen, color):
        rysuj(xcenter,ycenter,h.q,h.r,h.s,a, offset, screen, color)

    def dod_siada(h, inny):
        if (inny.q==h.q or inny.r==h.r or inny.s==h.s) and (inny.q==h.q +1 or inny.s==h.s +1 or inny.r==h.r +1) and(inny!=h):
            h.siedzi.append(inny)

    
#znowu funkcje
            
def daj_im_siadow(hex_list):
    for x in hex_list:
        for y in hex_list:
            x.dod_siada(y)
























        
    
    
