lista =[0,0]
for x in range(1,999999):
    lista.append(1)
for x in range(2,1000001):
    for y in range(x*x,1000001,x):
        if y < 1000000:
            
            lista[y] = 0
suma = 0
for x in range(2,len(lista)+1):
    if suma == 726:
        print(x-1)
        break
    if lista[x]==1: 
        suma=suma+1
