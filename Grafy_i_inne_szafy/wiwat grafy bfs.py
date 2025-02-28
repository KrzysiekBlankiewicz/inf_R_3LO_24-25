class Node:
    def __init__(self, id):
        self.id=id

    def dodajsom(self, som):
        self.som=som

a=Node("a")
b=Node("b")
c=Node("c")
d=Node("d")
e=Node("e")
f=Node("f")

a.dodajsom([b,c,d])
b.dodajsom([a,c,e])
c.dodajsom([a,b,e,f])
d.dodajsom([a])
e.dodajsom([b,c])
f.dodajsom([c])


visited=[]
def dfs(start, meta):
    print(start.id)
    global visited
    if start==meta:
        return [start.id]
    visited.append(start)
    for s in start.som:
        if s not in visited:
            tymc=dfs(s, meta)
            if  tymc!=False:
                return [start.id]+ tymc
    return False

print(dfs(d,f))
visited=[]
print(dfs(e,d))

visiteb=[]
def bfs(start, meta):
    print(start.id)
    global visiteb
    visiteb.append(start)
    id=0
    while visiteb[id]!=meta:
        a=visiteb[id]
        for s in a.som:
            if s not in visiteb:
                visiteb.append(s)
        id+=1
        if id>len(visiteb)-1:
            return False
    return "wiwat"

print('bfs(d,f)',bfs(d,f))
visiteb=[]
print(bfs(e,d))
        

   

