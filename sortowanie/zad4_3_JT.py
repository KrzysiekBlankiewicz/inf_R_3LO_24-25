file=open('dane4.txt').read().splitlines()
for i in file:
    ile=0
def SortW(lista):
    for i in range(1, len(lista)):
        k = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > k:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = k
    return lista

print(SortW(file))

