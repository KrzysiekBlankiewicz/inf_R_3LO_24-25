import time
import random

def beginning_pop():
    arr = []
    for i in range(lenn):
        arr.append(i)
    beginning_pop_start = time.time()
    for i in range(lenn):
        arr.pop(0)
    beginning_pop_end = time.time()
    return beginning_pop_end - beginning_pop_start

def random_pop(arr):
    arr = []
    for i in range(lenn):
        arr.append(i)
    random_pop_start = time.time()
    for i in range(lenn):
        arr.pop(random.randint(0,lenn))
    random_pop_end = time.time()
    return random_pop_end - random_pop_start

def end_pop():
    arr = []
    for i in range(lenn):
        arr.append(i)
    end_pop_start = time.time()
    for i in range(lenn):
        arr.pop(-1)
    end_pop_end = time.time()
    return end_pop_end - end_pop_start

#main
lenn = int(input("set array len: "))
print("array len set to " + str(lenn) + " succesfully! \n")
print("beginning pop time (arr.pop(0)) = " + str(beginning_pop()))
print("random pop time (arr.pop(random_randint(0, len(arr))) = " + str(random_pop()))
print("random pop time (arr.pop(random_randint(0, len(arr))) = " + str(end_pop()))

