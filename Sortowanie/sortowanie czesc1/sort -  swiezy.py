def bubble_sort(Lista):
    for n in range(len(Lista)-1):
        for i in range(len(Lista)-1-n):
            if Lista[i]>Lista[i+1]:
                a=Lista[i]
                Lista[i]=Lista[i+1]
                Lista[i+1]=a


def insert_sort(Lista):
    Lista2=[]
    Lista2.append(Lista[0])
    for i in range(len(Lista)-1):
        good=0
        n=0
        while good==0:
            if Lista[i+1]>=Lista2[len(Lista2)-1]:
                Lista2.append(Lista[i+1])
                good=1
                
            
            elif Lista[i+1]<Lista2[n]:
                a=Lista2[len(Lista2)-1]
                
                for x in range(len(Lista2)-n):
                    Lista2[len(Lista2)-x-1]=Lista2[len(Lista2)-x-2]
                    
                Lista2[n]=Lista[i+1]
                Lista2.append(a)
                good=1
                
            n+=1

    for i in range(len(Lista)):
        Lista[i]=Lista2[i]
    





kij=[2,4,6,222, 3,243432423,37049809, 4423423, 7,4,6,345,3,6,88,6,5,6675,4234]    
#bubble_sort(kij)
#print(kij)
abc(kij)
print(kij)
