def spawanie(lista):
    if len(lista) <= 1:
        return

    midas = len(lista) // 2
    lewy_twix = lista[:midas]
    prawy_twix = lista[midas:]
    spawanie(lewy_twix)
    spawanie(prawy_twix)

    x = 0
    d = 0
    e = 0
    while x < len(lewy_twix) and d < len(prawy_twix):
        if lewy_twix[x] < prawy_twix[d]:

            lista[e] = lewy_twix[x]
            x += 1
        else:



            lista[e] = prawy_twix[d]
            d += 1
        e += 1

    while x < len(lewy_twix):

        lista[e] = lewy_twix[x]
        x += 1
        
        e += 1

    while d < len(prawy_twix):
        lista[e] = prawy_twix[d]
        d += 1
        e += 1
    return lista

lista = [1,9,6,3,13]
print(spawanie(lista))

