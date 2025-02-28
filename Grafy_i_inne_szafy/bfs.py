class Node:
    def __init__(self,ID):
        self.ID=ID
    def addneighbour(self,neighbour):
        self.neighbour=neighbour

a=Node("a")
b=Node("b")
c=Node("c")
d=Node("d")
e=Node("e")
f=Node("f")

a.addneighbour([d,f,b])
b.addneighbour([e,a])
c.addneighbour([e])
d.addneighbour([a])
e.addneighbour([b,c])
f.addneighbour([a])

visited=[]

def bfs(start,destination):
    global visited
    steps = [start]
    if start==destination:
        return steps
    visited.append(start)
    for n in start.neighbour:
        if n not in visited:
            temp=bfs(n,destination)
            if temp != False:
                return steps + temp
    return False

steps = bfs(c,f)
print("steps:")
if steps == False:
    print ("Can't do it")
else:
    for i in range (len(steps)):
            steps[i] = steps[i].ID
            print (steps[i])
