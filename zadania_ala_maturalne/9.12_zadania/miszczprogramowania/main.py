def platformowka(a1,a2,b1,b2):
    if b1 <= a2 and b2 >=a1:
        print("b po prawej")
        if b1> a1 and b2>a2:
            return a2-b1 
        if b1>a1 and b2<a2:
            return b2-b1
        return abs(b2 - a1)
    if b1 <= a1 and b2 >=a2:
        print("b po lwej")
        if a1> b1 and a2>b2:
            return b2-a1
        if b2>a1 and a1>b2:
                return b2-a1
        return abs(a1 - b2)
    return "nie"
#print(platformowka(5,10,1,8))
#print(platformowka(5, 9, 1, 8))

def kucharz(lista):
    lista2 = []
    pier = lista[0]
    lista2.append(lista[1])
    for x in range(1,pier):
        el1 = lista[x]
        el2 = lista[x+1]
        lista2.append(el2-el1)
    return lista2
print(kucharz([3,1,100,101]))

def bez_kontekstu(lista):
    lista1= []
    licznik =0 
    jakis_belkot = list(lista[2])
    slowo = list(lista[3])
    for x in jakis_belkot:
        if sorted(slowo) == sorted(jakis_belkot[licznik:licznik+8]):
            lista1.append(licznik+1)
        licznik+=1
    return lista1

print(bez_kontekstu([12, 8,"kiercukiiker","cukierki"]))
