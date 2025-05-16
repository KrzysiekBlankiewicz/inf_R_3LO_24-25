w = [3,7,2,1,5]
d = -1

def horner(w, d):
    r = [w[0]]
    for i in range(1, len(w)):
        r.append(d*r[i-1]+w[i])
    return r

print(horner(w,d))
