import pygame
import graph as g

#modes:
idle = 0
node_place = 1
vertex_start = 2
vertex_end = 3

def mode_change(key):
    if key == pygame.K_n:
        return node_place
    if key == pygame.K_s:
        return vertex_start
    if key == pygame.K_e:
        return vertex_end
    return idle
    
def handle_click(mode, builder, position):
    x = position[0]
    y = position[1]
    result = False

    if mode == idle:
        builder.tempNode = None
    
    elif mode == node_place:
        builder.tempNode = None
        result = builder.new_node(x, y)
        
    elif mode == vertex_start:
        v = builder.get_node_at_pos(x, y)
        if v != None:
            builder.tempNode = v
            result = v.id
        else:
            result = False
            
    elif mode == vertex_end:
        v = builder.get_node_at_pos(x, y)
        if v != None:
            if builder.new_vertex(v):
                result = builder.to_string()
        else:
            result = False
            
    return result
        
size = 1000
pygame.init()
window = pygame.display.set_mode((size, size))
running = True
mode = idle

gb = g.GraphBuilder(size)

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            
        if e.type == pygame.KEYDOWN:
            mode = mode_change(e.key)
            print("in mode:" + str(mode))
            
        if e.type == pygame.MOUSEBUTTONUP:
            result = handle_click(mode, gb, e.pos)
            if result != False:
                print(result)

    window.fill((255, 255, 255))
    for n in gb.nodes:
        pygame.draw.circle(window, (0,0,0), (n.x, n.y), gb.node_radius)
        for nn in n.nghb:
            pygame.draw.line(window, (0,0,0), (n.x, n.y), (nn.x, nn.y))
        
    pygame.display.flip()

pygame.quit()
