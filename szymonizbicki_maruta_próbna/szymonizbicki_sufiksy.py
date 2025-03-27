p1 = open("slowa1.txt").readlines()
p2 = open("slowa2.txt").readlines()
p3 = open("slowa3.txt").readlines()
n1 = p1[0]
n2 = p2[0]
n3 = p3[0]
s1 = []
s2 = []
s3 = []
for x in range(len(p1[1])-1):
    s1.append(p1[1][x])
for x in range(len(p2[1])-1):
    s2.append(p2[1][x])
for x in range(len(p3[1])-1):
    s3.append(p3[1][x])
k11 = p1[2][0]
k12 = p1[2][2]
k21 = p2[2][0]
k22 = p2[2][2]
k31 = p3[2][0]
k32 = p3[2][2]



def czy_mniejszy(n, s, k1, k2):
    global porownania
    i = k1
    j = k2
    while (i <= n and j <= n):
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return "TAK"
            else:
                return "NIE"
    if j <= n:
        return "TAK"
    else:
        return "NIE"

print(czy_mniejszy(n1, s1, k11, k12))