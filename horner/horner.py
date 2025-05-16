def Horner(W,d):
    R=[]
    R.append(W[0])
    for i in range(1,len(W)):
        a=R[len(R)-1]*d+W[i]
        R.append(a)
    return R

print(Horner([3,7,2,1,5], -1))
