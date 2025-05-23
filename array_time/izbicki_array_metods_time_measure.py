#Szymon Izbicki

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

def random_pop():
    arr = []
    for i in range(lenn):
        arr.append(i)
    random_pop_start = time.time()
    for i in range(lenn):
        arr.pop(random.randint(0,len(arr)-1))
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

def begininng_insert():
    arr = []
    beginning_insert_start = time.time()
    for i in range(lenn):
        arr.insert(0, 1)
    beginning_insert_end = time.time()
    return beginning_insert_end - beginning_insert_start

def random_insert():
    arr = [1]
    random_insert_start = time.time()
    for i in range(lenn):
        arr.insert(random.randint(0,len(arr)-1), 1)
    random_insert_end = time.time()
    return random_insert_end - random_insert_start

def end_insert():
    arr = []
    end_insert_start = time.time()
    for i in range(lenn):
        arr.append(1)
    end_insert_end = time.time()
    return end_insert_end - end_insert_start
    
#main
lenn = int(input("set array len: "))
print("array len set to " + str(lenn) + " succesfully! \nHere are measurements for each function: \n")
print("beginning pop time (arr.pop(0)) = " + str(beginning_pop()))
print("random pop time (arr.pop(random.randint(0,len(arr)-1))) = " + str(random_pop()))
print("end pop time (arr.pop(-1) = " + str(end_pop()))
print("beginning insert time (arr.insert(0, 1)) = " + str(begininng_insert()))
print("random insert time (arr.insert(random_randint(0,len(arr)-1), 1) = " + str(random_insert()))
print("end insert time (arr.append(1)) = " + str(end_insert()))
