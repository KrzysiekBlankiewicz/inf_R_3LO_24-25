

def obliczajONP(wyr):
    lista=[]
    for x in wyr:
        if type(x) is int:
            lista.append(x)
        elif type(x) is str:
            a=lista[len(lista)-2]
            b=lista[len(lista)-1]
            c=0
            if x == '+':
                c=a+b
            elif x =='-':
                c=a-b
            elif x =='*':
                c=a*b
            elif x =='/':
                c=a/b

            lista.pop()
            lista.pop()
            lista.append(c)
    if len(lista)==1:
        return lista[0]


m=[27, 32, '+', 23, 43, '+', '-']

print(obliczajONP(m))

