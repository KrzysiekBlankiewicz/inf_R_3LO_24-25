def kloce (a1,a2,b1,b2):

    
    if a1 < b1:
        if a2 == b1:
            print("stykają się")
            return 0         
        if a2 < b1:
            print('nie byq')
        if a2 > b1:
            print('yessir byq')
            return abs(a2) - abs(b1) 
    else:
        if a1 > b1:
            if b2 == a1:
                print("stykają się")
                return 0         
            elif b2 < a1:
                print('nie bykq')
            elif a1 > b2:
                print('yessir byq')
                return abs(b2) - abs(a1)
    return 2222


print(kloce(4, 6, 2, 8))
