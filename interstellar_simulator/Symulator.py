import pygame
import Kolory as k
import Rakieta as r
import Planety as p


red = (255, 0, 0)
screenX = 1900
screenY = 1000

pygame.init()
screen = pygame.display.set_mode((screenX, screenY))

juno = r.Rocket(3625, 950, 500)
ganimedes = p.Planet(1.4819*10**23, 444, 333, k.purple, 52*2)
kallisto = p.Planet(1.07594*10**23, 765,765, k.blue, 24*2)
io = p.Planet(8.93*10**22, 1420,666, k.yellow, 36*2)
europa = p.Planet(4.80*10**22, 1234, 213, k.red, 15*2)

print("Pingwin - Ganimedes", juno.grav(ganimedes))
print("Pingwin - Kallisto", juno.grav(kallisto))
print("Pingwin - Io", juno.grav(io))
print("Pingwin - Europa", juno.grav(europa))

#wektor do Ganimedesa
gY = juno.posY - ganimedes.posY
gX = juno.posX - ganimedes.posX
Fx = juno.grav(ganimedes) * gX /100000000000
Fy = juno.grav(ganimedes) * gY /100000000000
print(Fx, Fy)
print("dX =", gX)
print("dY =", gY)




running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(k.black)

    juno.draw(screen)
    ganimedes.draw(screen)
    kallisto.draw(screen)
    io.draw(screen)
    europa.draw(screen)

    pygame.draw.line(screen, k.purple, (juno.posX, juno.posY), (Fx, Fy), 2)

    pygame.display.flip()

pygame.quit()

