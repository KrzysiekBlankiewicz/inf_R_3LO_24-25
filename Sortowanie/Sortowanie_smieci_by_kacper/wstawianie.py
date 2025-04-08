def wstawanie(lista):
    
    for x in range(1,len(lista)): 
        pom = lista[x]
        xd = x - 1
        while xd > 0 and lista[xd] > pom:
            lista[xd + 1] = lista[xd]
            xd = xd - 1
        lista[xd + 1] = pom
    return lista


posortowana = wstawanie([1,9,6,3,13])
print(posortowana)
