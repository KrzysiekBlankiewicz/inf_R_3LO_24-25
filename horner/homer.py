def hornet(w,d):
    wyjscie = []
    wyjscie.append(w[0])
    l = w[0] 
    for i in range(1,len(w)):
        l = w[i] + l*d
        wyjscie.append(l)

    return  wyjscie

wilelonian = [3,7,2,1,5]


print(hornet(wilelonian,-1))