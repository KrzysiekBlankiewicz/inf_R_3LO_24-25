import math
import pygame
import hexagon

class pionek:

    def __init__(p, hex):
        p.hex=hex

    def rysuj_piona(p, screen, color, a,xcenter, ycenter):
        wsp=p.hex.daj_pion_pos( xcenter,ycenter,a)
        pygame.draw.circle(screen, color, (wsp),a/2)

    def kontrol_ruch(p,event):
        if event.key == pygame.K_q:
            for x in p.hex.siedzi:
                print(x.s)
                if x.s-1==p.hex.s:
                    p.hex=x
                    print(p.hex)
        elif event.key == pygame.K_d:
            for x in p.hex.siedzi:
                if x.s+1==p.hex.s:
                    p.hex=x
        elif event.key == pygame.K_e:
            for x in p.hex.siedzi:
                if x.r+1==p.hex.r:
                    p.hex=x
        elif event.key == pygame.K_a:
            for x in p.hex.siedzi:
                if x.r-1==p.hex.r:
                    p.hex=x
        elif event.key == pygame.K_w:
            for x in p.hex.siedzi:
                if x.q+1==p.hex.q:
                    p.hex=x
        elif event.key == pygame.K_s:
            for x in p.hex.siedzi:
                if x.q-1==p.hex.q:
                    p.hex=x
                
