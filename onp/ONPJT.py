def onp(lista):
    stos = [] 
    for i in lista:
        if i.isdigit(): 
            n = int(i)
            stos.append(n) 
        else:
            x = stos.pop() 
            y = stos.pop()
            if i == '*':
                stos.append(y*x) 
            elif i == '-':
                stos.append(y-x) 
            elif i == '+':
                stos.append(y+x) 
            else:
                stos.append(y//x)
    return stos[0]
print(onp(['2', '1', '+', '3', '*'])) 
