class Node:
    def __init__(self,id):
        self.id = id
    def add_soms(self,soms):
        self.soms = soms

x = Node("x")
y = Node("y")
z = Node("z")
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

x.add_soms([a,c,y])
y.add_soms([b,x])
z.add_soms([b])
a.add_soms([x])
b.add_soms([d,z,y])
c.add_soms([x])
d.add_soms([b])
for i in c.soms:
    print(i.id)

visited = []
    
def bfs(start,dest):
    global visited
    visited.append(start)
    print(start.id)
    if start == dest:
        return [start.id]
    for s in start.soms:
        if s not in visited:
            temp = bfs(s,dest)
            if temp != False:
                return [start.id]+temp
    return False




print(bfs(c,z))