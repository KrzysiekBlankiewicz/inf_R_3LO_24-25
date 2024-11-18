import math
import pygame
import hexagon

class ruszator:
    def __init__(r, keys):
        r.q = keys[0]
        r.w = keys[1]
        r.e=keys[2]
        r.a=keys[3]
        r.s=keys[4]
        r.d=keys[5]

        

class pionek:

    def __init__(p, hex, kolor, ruszator, kolor_dawany, literka):
        p.hex=hex
        p.kolor=kolor
        p.ruszator = ruszator
        p.kolor_dawany=kolor_dawany
        p.literka=literka
       
        

    def rysuj_piona(p, screen, a,xcenter, ycenter):
        wsp=p.hex.daj_pion_pos( xcenter,ycenter,a)
        p.hex.zajmij(p.literka, p.kolor_dawany)
        pygame.draw.circle(screen, p.kolor, (wsp),a/2)

    def kontrol_ruch(p,event):
        if event.key == p.ruszator.e:
            for x in p.hex.siedzi:
                if x.s+1==p.hex.s and x.r==p.hex.r:
                    p.hex=x
        elif event.key == p.ruszator.a:
            for x in p.hex.siedzi:
                if x.s-1==p.hex.s  and x.r==p.hex.r:
                    p.hex=x
        elif event.key == p.ruszator.q:
            for x in p.hex.siedzi:
                if x.r-1==p.hex.r and x.s==p.hex.s:
                    p.hex=x
        elif event.key == p.ruszator.d:
            for x in p.hex.siedzi:
                if x.r+1==p.hex.r and x.s==p.hex.s:
                    p.hex=x
        elif event.key == p.ruszator.w:
            for x in p.hex.siedzi:
                if x.s+1==p.hex.s and x.q==p.hex.q:
                    p.hex=x
        elif event.key == p.ruszator.s:
            for x in p.hex.siedzi:
                if x.s-1==p.hex.s and x.q==p.hex.q:
                    p.hex=x
        
