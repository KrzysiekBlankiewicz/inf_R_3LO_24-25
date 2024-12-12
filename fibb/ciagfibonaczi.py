def fibo(n):
    if n==1 or n==2:
        output=1
    else:
        output = fibo(n-1) + fibo(n-2)
    return output
print (fibo(6))
