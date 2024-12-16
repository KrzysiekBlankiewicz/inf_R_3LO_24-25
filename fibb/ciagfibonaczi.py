import time as t


def fibo(n):
    if n==1 or n==2:
        output=1
    else:
        output = fibo(n-1) + fibo(n-2)
    return output


time0 = t.time()

print(fibo(45))
      
time1 = t.time()

print(time1-time0)
