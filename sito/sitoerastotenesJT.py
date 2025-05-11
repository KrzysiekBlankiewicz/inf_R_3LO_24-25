def erastotenes(n):
    sito = [1] * (n + 1)
    sito[0] = sito[1] = 0  

    for i in range(2, int(n ** 0.5) + 1):
        if sito[i] == 1:
            for j in range(i * i, n + 1, i):
                sito[j] = 0  

    pierwsze = []
    for i in range(len(sito)):
        if sito[i] == 1:
            pierwsze.append(i)

    return pierwsze

pierwsze = erastotenes(6000)
print(pierwsze[725])
