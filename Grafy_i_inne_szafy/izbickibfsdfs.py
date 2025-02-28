visited = []

class Node:
    def __init__(self, id):
        self.id = id
    def add_soms(self, soms):
        self.soms = soms

a = Node("a")
b = Node("b")
c = Node("c")  
d = Node("d")
e = Node("e")
f = Node("f")

a.add_soms([a,b,c,e,f])
b.add_soms([a,b,c,e,f])
c.add_soms([a,b,c,e,f])
d.add_soms([a,b,c,e,f])
e.add_soms([a,b,c,e,f])
f.add_soms([a,b,c,e,f])

def dfs(start, dest):
    global visited
    route = [start]
    if start == dest:
        return route
    visited.append(start)
    for s in start.soms:
        if s not in visited:
            temp = dfs(s,dest)
            if temp != False:
                return route + temp
    return False

def bfs(start, dest):
    lista = [start]
    id = 0
    while lista[id] != dest:
        if soms not in lista[id]:
        lista[id].append(soms)
    id+=1
    if wyszedl za liste:
        False


route = dfs(a, d)
if route != False:
    print("route:")
    for i in range(len(route)):
        route[i] = route[i].id
        print(route[i])
else:
    print("Error 404: no route found!")