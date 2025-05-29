class Stos:
    def __init__(s):
        s.size=0
        s.tablica=[]
        
        

    def pop(s):
        if s.size>0:
            s.size-=1
            return s.tablica.pop()
        return 'gościu ten stos jest pusty'

    def na_stos(s, value):
        s.tablica.append(value)
        s.size+=1
        
        

    def podejrz(s):
        if s.size>0:
            return s.tablica[len(s.tablica)-1]
        else:
            return 'gościu ten stos jest pusty'
    

a=Stos()        
for x in range(10):
    a.na_stos(2**x)
    
