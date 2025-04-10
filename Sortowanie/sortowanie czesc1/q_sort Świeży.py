def q_sort(Lista):
    

    if len(Lista)<2:
        return Lista
    if len(Lista)==2:
        if Lista[0]>Lista[1]:
            lista[0],Lista[1]=Lista[1], Lista[0]
        return Lista
    
    mini=Lista[0]
    for x in Lista:
        if x<mini:
            mini=x
    
    i=0
    while Lista[i]==mini:
        i+=1
    pivot= Lista[i]
    lewe=[]
    prawe=[]
    for x in Lista:
        
        if x>=pivot:
            prawe.append(x)
        else:
            lewe.append(x)
    

    a=q_sort(lewe)
    b=q_sort(prawe)
    Lista= a+b
    return Lista



kij=[1,3,5,7,56,7856,986,456,456,786,9,79,3456,423, 123]

print(q_sort(kij))
