import math
import pygame
import hexagon

class ruszator:
    def __init__(r, keys):
        r.r_up = keys[0]
        r.r_down = keys[1]
        r.q_up=keys[2]
        r.q_down=keys[3]
        r.s_up=keys[4]
        r.s_down=keys[5]

        

class pionek:

    def __init__(p, hex, kolor, ruszator):
        p.hex=hex
        p.kolor=kolor
        p.ruszator = ruszator
        

    def rysuj_piona(p, screen, a,xcenter, ycenter):
        wsp=p.hex.daj_pion_pos( xcenter,ycenter,a)
        pygame.draw.circle(screen, p.kolor, (wsp),a/2)

    def kontrol_ruch(p,event):
        if event.key == p.ruszator.r_up:
            for x in p.hex.siedzi:
                if x.s+1==p.hex.s and x.r==p.hex.r:
                    p.hex=x
        elif event.key == p.ruszator.r_down:
            for x in p.hex.siedzi:
                if x.s-1==p.hex.s  and x.r==p.hex.r:
                    p.hex=x
        elif event.key == p.ruszator.s_up:
            for x in p.hex.siedzi:
                if x.r-1==p.hex.r and x.s==p.hex.s:
                    p.hex=x
        elif event.key == p.ruszator.q_down:
            for x in p.hex.siedzi:
                if x.r+1==p.hex.r and x.s==p.hex.s:
                    p.hex=x
        elif event.key == p.ruszator.q_up:
            for x in p.hex.siedzi:
                if x.s+1==p.hex.s and x.q==p.hex.q:
                    p.hex=x
        elif event.key == p.ruszator.q_down:
            for x in p.hex.siedzi:
                if x.s-1==p.hex.s and x.q==p.hex.q:
                    p.hex=x
                
