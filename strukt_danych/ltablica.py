import random
import time


def generator(dlugosc):
    tab = []
    for x in range(dlugosc):
        tab.append(1)
    return tab

def dodawani_na_poczatku(dlugosc):
    tab = generator(dlugosc)
    start = time.time()
    for x in range(dlugosc):
        tab.pop(0)
    end = time.time()
    wynik = end - start
    return wynik

def usuwanie_na_koncu(dlugosc):
    tab = generator(dlugosc)
    start = time.time()
    for x in range(dlugosc):
        tab.pop(-1)
    end = time.time()
    wynik = end - start
    return wynik

def losowe_usuwnie(dlugosc):
    tab = generator(dlugosc)
    start = time.time()
    for i in range(dlugosc):
        tab.pop(random.randint(0,len(tab)-1))
    end = time.time()
    wynik = end - start
    return wynik


def dodawanie_na_poczatku(dlugosc):
    tab = generator(dlugosc)
    start = time.time()
    for i in range(dlugosc):
        tab.insert(0, 1)
    end = time.time()
    wynik = end - start
    return wynik

def dodawanie_losowe(dlugosc):
    tab = [1]
    start = time.time()
    for i in range(dlugosc):
        tab.insert(random.randint(0,len(tab)-1), 1)
    end = time.time()
    wynik = end - start
    return wynik

def dodawanie_na_koncu(dlugosc):
    tab = []
    start = time.time()
    for i in range(dlugosc):
        tab.append(1)
    end = time.time()
    wynik = end - start
    return wynik

def index(dlugosc):
    tab = []
    for i in range(dlugosc):
        tab.append(i)
    losowa_liczba = random.choice(tab)
    start = time.time()
    tab.index(losowa_liczba)
    end = time.time()
    wynik = end - start
    return wynik

print(dodawanie_losowe(1000000))