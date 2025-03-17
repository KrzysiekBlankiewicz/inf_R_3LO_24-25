import pygame
import graph as g
import os

#modes:
idle = 0
node_place = 1
vertex_start = 2
vertex_end = 3

def mode_change(key):
    if key == pygame.K_1:
        return node_place
    if key == pygame.K_2:
        return vertex_start
    if key == pygame.K_3:
        return vertex_end
    return idle

def handle_click(mode, builder, position):
    x, y = position
    result = False

    if mode == idle:
        builder.tempNode = None
    elif mode == node_place:
        builder.tempNode = None
        result = builder.new_node(x, y)
    elif mode == vertex_start:
        v = builder.get_node_at_pos(x, y)
        if v is not None:
            builder.tempNode = v
            result = v.id
    elif mode == vertex_end:
        v = builder.get_node_at_pos(x, y)
        if v is not None:
            if builder.new_vertex(v):
                result = builder.to_string()
    
    return result

def dopliku(builder, filename="danegraph.txt"):
    with open(filename, 'w') as f:
        f.write(builder.to_string())

def zpliku(builder, filename="danegraph.txt"):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = f.read()
            builder.from_string(data)

size = 1000
pygame.init()
window = pygame.display.set_mode((size, size))
running = True
mode = idle

gb = g.GraphBuilder(size)
zpliku(gb)

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            mode = mode_change(e.key)
            print("in mode:", mode)
        if e.type == pygame.MOUSEBUTTONUP:
            result = handle_click(mode, gb, e.pos)
            if result:
                print(result)
                dopliku(gb)

    window.fill((255, 255, 255))
    for n in gb.nodes:
        pygame.draw.circle(window, (0,0,0), (n.x, n.y), gb.node_radius)
        for nn in n.nghb:
            pygame.draw.line(window, (150,0,255), (n.x, n.y), (nn.x, nn.y), 7)
    
    pygame.display.flip()

pygame.quit()
