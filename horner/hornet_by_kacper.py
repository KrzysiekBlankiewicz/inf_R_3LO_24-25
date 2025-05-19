def hornet(w,d):
    R = [0]
    R[0]=w[0]
    for x in range(1,len(w)):
        R.append(w[x]+R[x-1]*d)
    return R

print(hornet([3,7,2,1,5],-1))