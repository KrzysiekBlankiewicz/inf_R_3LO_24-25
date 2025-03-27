f = open("przyklad.txt").readlines()
for i in range(len(f)):
    f[i] = f[i][0:-1]

def czy_zrownowazona(f):
    zrownowazone_count = 0
    prawiezrowanowazone_count = 0
    for i in range(len(f)):
        count1 = 0
        count0 = 0
        for j in range(len(f[i])):
            if f[i][j] == '0':
                count0 += 1
            else:
                count1 += 1
        if count0 == count1:
            zrownowazone_count += 1
        elif count1+1 == count0 or count0+1 == count1:
            prawiezrowanowazone_count += 1
    return zrownowazone_count, prawiezrowanowazone_count

print(czy_zrownowazona(f))