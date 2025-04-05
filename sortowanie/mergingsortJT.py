def mergesort(lista):
    if len(lista) <= 1:
        return lista

    srodek = len(lista) // 2
    lewa = mergesort(lista[:srodek])
    prawa = mergesort(lista[srodek:])

    wynik = []
    i = j = 0

    while i < len(lewa) and j < len(prawa):
        if lewa[i] < prawa[j]:
            wynik.append(lewa[i])
            i += 1
        else:
            wynik.append(prawa[j])
            j += 1

    wynik += lewa[i:]
    wynik += prawa[j:]

    return wynik


lista = [9, 2, 3, 4, 5, 6, 7, 8, 1]
print(mergesort(lista))
