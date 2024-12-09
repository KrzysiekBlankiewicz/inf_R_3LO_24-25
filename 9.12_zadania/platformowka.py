import math
def nachodzenie(a1,a2,b1,b2):
    if a2<b1:
        return ("NIE")
    if b2<a1:
        return ("NIE")
    if a1<=b1 and b2<=a2 or b1<=a1 and a2<=b2:
        n=abs((b2-b1)-(a2-a1))
        return n
    if a1 == b2 or b1 == a2:
        return 0
    
print (nachodzenie(11,12,11,20))



def kucharz(lista):
    list=[]
    lista.remove(lista[0])
    list.append(lista[0])
    for i in range(len(lista)-1):
        list.append(lista[i+1]-lista[i])
    return list

print (kucharz([1,100,101,200]))


def anagram(a,b,wyraz,fragment):
    wyraz=split(wyraz)
    litery=sort(wyraz)
    


