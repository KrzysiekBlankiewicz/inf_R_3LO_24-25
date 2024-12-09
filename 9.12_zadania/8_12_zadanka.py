def platformówka(a1, a2, b1, b2):
    if a2 > b1 and a1 < b2:
        return a2 - b1
    elif a1 < b1 and b2 < a2:
        return b2 - b1
    elif b1 < a1 and a2 < b2:
        return a2 - a1
    elif b1 < a1 and b2 < a2:
        return b2 - a2
    elif b2 > a1 and b1 < a1:
        return b2 - a1
    else:
        return 'nie' 
def kucharz(list):
    del list[0]
    result = [list[0]]
    for i in range(len(list)-1):
        result.append(list[i+1] - list[i])
    return result
