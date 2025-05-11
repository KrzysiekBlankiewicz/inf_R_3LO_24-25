lista = []
for l in range(100000):
    lista.append(1)





def sito(t,n):
    wyjscie = []
    for i in range(2,len(t)):
        if i == 1:
            wyjscie.append(i)
        for k in range(i,n//i):
            t[k*i] = 0
    return wyjscie


print(sito(lista,100000))

#nie działa mi :c