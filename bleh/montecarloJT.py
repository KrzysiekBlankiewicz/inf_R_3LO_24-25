import random

def montecarlo(n):
    trafione = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            trafione += 1
    return 4 * trafione / n

print("Przybliżone pi:", montecarlo(10))
