class punkt:
    def __init__(self,id,posx,posy):
        self.id = id
        self.posx = posx
        self.posy = posy
    def somsiad(self,soms):
        self.soms = soms


x = punkt("x")
y = punkt("y")
z = punkt("z")
a = punkt("a")
b = punkt("b")
c = punkt("c")
d = punkt("d")

x.somsiad([a,c,y])
y.somsiad([b,x])
z.somsiad([b])
a.somsiad([x])
b.somsiad([d,z,y])
c.somsiad([x])
d.somsiad([b])


