import pygame
import Kolory as k
import Rakieta as r
import Planety as p


screenX = 1900
screenY = 1000

pygame.init()
screen = pygame.display.set_mode((screenX, screenY))

juno = r.Rocket(3625, 950, 500, 0, 0)
ganimedes = p.Planet(1.4819*10**23, 444, 333, k.purple, 52*2)
kallisto = p.Planet(1.07594*10**23, 765,765, k.blue, 24*2)
io = p.Planet(8.93*10**22, 1420,666, k.yellow, 36*2)
europa = p.Planet(4.80*10**22, 1234, 213, k.red, 15*2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(k.black)

    juno.draw(screen) #Rakieta
    ganimedes.draw(screen)
    kallisto.draw(screen)
    io.draw(screen)
    europa.draw(screen)

    gFx = juno.grav(ganimedes) * (ganimedes.posX - juno.posX) / 10**12
    gFy = juno.grav(ganimedes) * (ganimedes.posY - juno.posY) / 10**12
    kFx = juno.grav(kallisto) * (kallisto.posX - juno.posX) / 10**12
    kFy = juno.grav(kallisto) * (kallisto.posY - juno.posY) / 10**12
    iFx = juno.grav(io) * (io.posX - juno.posX) / 10**12
    iFy = juno.grav(io) * (io.posY - juno.posY) / 10**12
    eFx = juno.grav(europa) * (europa.posX - juno.posX )/ 10**12
    eFy = juno.grav(europa) * (europa.posY - juno.posY) / 10**12
    FwypX = gFx + kFx + iFx + eFy
    FwypY = gFy + kFy + iFy + eFy

    juno.draw_Fwyp(screen, FwypX, FwypY)
    juno.acceleration(FwypX, FwypY)
    juno.velocity()
    juno.move()

#próbowałem z listą, ale coś mi nie wyszło, więc zrobiłem ręcznie :/

    #czasami jak rakieta za szybko przeleci przez planetę (w jednej klatce), to program tego nie wyłapie, ale nie dokońca wiem, jak to naprawić :(
    if juno.posX + juno.radius/2 >= ganimedes.posX - ganimedes.radius/2 and juno.posX + juno.radius/2 <= ganimedes.posX + ganimedes.radius/2:
        if juno.posY + juno.radius/2 >= ganimedes.posY - ganimedes.radius/2 and juno.posY +juno.radius/2 <= ganimedes.posY + ganimedes.radius/2:
            print("UWAGA! ZDERZENIE Z GANIMEDESEM! Uruchamianie teleportacji z dala od zagrożenia...")
            juno.teleport_start(screen)
            juno.teleport()
            juno.teleport_end(screen)
    if juno.posX + juno.radius/2 >= kallisto.posX - kallisto.radius/2 and juno.posX + juno.radius/2 <= kallisto.posX + kallisto.radius/2:
        if juno.posY + juno.radius/2 >= kallisto.posY - kallisto.radius/2 and juno.posY +juno.radius/2 <= kallisto.posY + kallisto.radius/2:
            print("UWAGA! ZDERZENIE Z KALLISTO! Uruchamianie teleportacji z dala od zagrożenia...")
            juno.teleport_start(screen)
            juno.teleport()
            juno.teleport_end(screen)
    if juno.posX + juno.radius/2 >= io.posX - io.radius/2 and juno.posX + juno.radius/2 <= io.posX + io.radius/2:
        if juno.posY + juno.radius/2 >= io.posY - io.radius/2 and juno.posY +juno.radius/2 <= io.posY + io.radius/2:
            print("UWAGA! ZDERZENIE Z IO! Uruchamianie teleportacji z dala od zagrożenia...")
            juno.teleport_start(screen)
            juno.teleport()
            juno.teleport_end(screen)
    if juno.posX + juno.radius/2 >= europa.posX - europa.radius/2 and juno.posX + juno.radius/2 <= europa.posX + europa.radius/2:
        if juno.posY + juno.radius/2 >= europa.posY - europa.radius/2 and juno.posY +juno.radius/2 <= europa.posY + europa.radius/2:
            print("UWAGA! ZDERZENIE Z EUROPĄ! Uruchamianie teleportacji z dala od zagrożenia...")
            juno.teleport_start(screen)
            juno.teleport()
            juno.teleport_end(screen)




    pygame.display.flip()

pygame.quit()


#pygame.draw.line(screen, k.purple, (juno.posX, juno.posY), (juno.posX + gFx, juno.posY + gFy), 2)
#pygame.draw.line(screen, k.blue, (juno.posX, juno.posY), (juno.posX + kFx, juno.posY + kFy), 2)
#pygame.draw.line(screen, k.yellow, (juno.posX, juno.posY), (juno.posX + iFx, juno.posY + iFy), 2)
#pygame.draw.line(screen, k.red, (juno.posX, juno.posY), (juno.posX + eFx, juno.posY + eFy), 2)