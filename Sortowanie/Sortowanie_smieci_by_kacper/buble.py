def bubble(lista):
    n = len(lista)


    while n > 1:
        for i in range(n-1):

            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]  

        n = n-1

    return lista

lista = [1,9,6,3,13]
print(bubble(lista))
