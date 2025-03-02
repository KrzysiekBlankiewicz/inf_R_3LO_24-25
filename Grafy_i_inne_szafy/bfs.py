class Node:
    def __init__(self, ID):
        self.ID = ID
    def addneighbour(self, neighbour):
        self.neighbour = neighbour  

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")

a.addneighbour([d, f, b])
b.addneighbour([e, a])
c.addneighbour([e])
d.addneighbour([a])
e.addneighbour([b, c])
f.addneighbour([a])

def bfs(start, destination):
    steps = [[start]]  
    id = 0
    visited = []  

    while id < len(steps):
        path = steps[id]  
        node = path[-1]  

        if node == destination:
            return path  

        if node not in visited:
            visited.append(node)  
            for neighbour in node.neighbour:
                if neighbour not in visited:
                    steps.append(path + [neighbour])  

        id += 1

    return False 

steps = bfs(d, f)
print("steps:")
if steps == False:
    print("Can't do it")
else:
    for node in steps:
        print(node.ID)



