def horner(w,d):
    R=[]
    R.append(w[0])
    for i in range(1,len(w)):
        x=w[i]+R[i-1]*d
        R.append(x)
    return R
w=[3,7,2,1,5]
d=-1
print(horner(w,d))
        
        
                   
