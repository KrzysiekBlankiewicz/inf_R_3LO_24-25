import math
import random

xx = []
yy = []

r = 100
w = 0
p = 1000000

def pitagey(x,y):
    wyjscie = math.sqrt(x**2+y**2)
    return wyjscie


for i in range(1,p):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    xx.append(x)
    yy.append(y)

for x in range(0,len(xx)):
    if abs(pitagey(xx[x],yy[y])) <= 100:
        w += 1
 
pi = (4*w)/p 
print(pi)
#no wy miare działa
#https://youtu.be/cuxujgpr8Zk
