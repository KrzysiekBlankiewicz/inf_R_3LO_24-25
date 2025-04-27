listaaaaa = [7,1,3,5,2,8,17,142,7132,666,-3]


def wybor(t):
    i = 0
    while i < len(t):
        x = min(t[i:len(t)])
        t.remove(x)
        t.insert(i,x)
        i += 1
    return t

print(wybor(listaaaaa),"przez wybór")
listaaaaa = [7,1,3,5,2,8,17,142,7132,666,-3]

def sortowanie(p,l):
    
    kniec = []
    i  = 0
    j = 0
    while i < len(l) and j < len(p):
        if l[i] < p[j]:
            kniec.append(l[i])
            i += 1
        else:
            kniec.append(p[j])
            j += 1
    kniec.extend(l[i:])
    kniec.extend(p[j:])
    return kniec

def spawnie(t):
    if len(t) <= 1:
        return t

    
    
    polowa = len(t)//2
    prawa = t[polowa:]
    lewa = t[:polowa]
    
    dobraprawa = spawnie(prawa)
    dobralewa = spawnie(lewa)

    return sortowanie(dobraprawa,dobralewa)

print(spawnie(listaaaaa),"przez spawanie")
listaaaaa = [7,1,3,5,2,8,17,142,7132,666,-3]

def bomblek(t):
    i = 0
    d = len(t) - 1 - i
    while i <= len(t):
        for k in range(0,d):
            if t[k] > t[k+1]:
                x = t[k+1]
                t.remove(x)
                t.insert(k,x)
        i +=1
    return t

print(bomblek(listaaaaa),"bombelkowe")
listaaaaa = [7,1,3,5,2,8,17,142,7132,666,-3]
def wstawinie(t):
    for i in range(1,len(t)):
        x = t[i]
        j = i - 1 
        while j >= 0 and t[j] > x:
            t[j+1] = t[j]
            j -= 1
        t[j + 1] = x
    return t

print(wstawinie(listaaaaa),"przez wstawianie")
listaaaaa = [7,1,3,5,2,8,17,142,7132,666,-3]

def szybko(t):
    if len(t) <= 1:
        return t

    
    
    polowa = t[len(t)//2]
    prawa = t[polowa:]
    lewa = t[:polowa]
    
    dobraprawa = spawnie(prawa)
    dobralewa = spawnie(lewa)

    return sortowanie(dobraprawa,dobralewa)


print(szybko(listaaaaa),"quick sort (moze byc cos nie tak w kodzie)")