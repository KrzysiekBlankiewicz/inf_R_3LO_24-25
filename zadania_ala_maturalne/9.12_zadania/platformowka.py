def nachodzenie(a1, a2, b1, b2):
    if a2 < b1 or b2 < a1: 
        return "NIE"
    if a1 == b2 or b1 == a2:  
        return 0  
    return min(a2, b2) - max(a1, b1)  

print(nachodzenie(11, 21, 22, 22))


def kucharz(lista):
    list=[]
    lista.remove(lista[0])
    list.append(lista[0])
    for i in range(len(lista)-1):
        list.append(lista[i+1]-lista[i])
    return list

print (kucharz([1,100,101,200]))


def anagram(n, m, wyraz, fragment):
    szukany_sort = ''.join(sorted(fragment))
    wynik = [i + 1 for i in range(n - m + 1) if ''.join(sorted(wyraz[i:i + m])) == szukany_sort]


print(anagram(12, 8, "kiercukiiker", "cukierki"))
    


