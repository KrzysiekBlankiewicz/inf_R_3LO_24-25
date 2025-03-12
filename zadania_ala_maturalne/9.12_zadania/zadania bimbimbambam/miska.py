
def miska(n,lista):
    lista2 =[]
    
    if lista[0] > lista[1]:
        print("gilgamesz złamał system ide popełnić zbrodnie wojenne w bośni i hercegowinie")
    
    else:
        for x in range (1,n):
            podmianaka = 0
            podmianaka = lista[n-x] - lista[n-x-1]
            lista2.append(podmianaka)
    lista2.append(lista[0])
    lista2.reverse()
    print(lista2)

print(miska(6,[5, 6 ,7, 16, 20, 23]))