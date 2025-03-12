def platformówka(a1,a2,b1,b2):
    if b1<=a2 and b1>=a1:
        if b2<=a2 and b2>=a1:
            return abs(b1-b2)
        if b2<a1:
            return abs(b1-a1)
        if b2>a2:
            return abs(b1-a2)
    if a1<=b2 and a1>=b1:
        if a2<=b2 and a2>=b1:
            return abs(a1-a2)
        if a2<b1:
            return abs(a1-b1)
        if b2>a2:
            return abs(a1-b2)
    else:
        return "NIE"

def kucharz(n, Lista):
    if n != len(Lista):
        return "baj baj"
    Lista2=[]
    Lista2.append(Lista[0])
    print(Lista2)
    for i in range (1,n):
        Lista2.append(Lista[i]-Lista[i-1])
        print(Lista2)
    return Lista2
    
def bezkontekstu(d1, d2, wyraz1, wyraz2):
    Lista=[]
    for n in range(d1-d2):
        for i in range(n, d2):
            Lista.append(wyraz1[i])
            
    
    







print(platformówka(1,8,5,10))

print(platformówka(3,8,9,10))

print(platformówka(1,8,5,10))
print(platformówka(-1,1,-5,1))

print(platformówka(-10000,10000,-10000,10000))


print(kucharz(6, (5, 6, 7, 16, 20, 23)))
