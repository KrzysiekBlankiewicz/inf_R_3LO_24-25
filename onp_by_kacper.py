def onp(lista):
    styrta = [] 
    for i in lista:
        if i.isdigit(): 
            n = int(i)

            styrta.append(n) 
        else:



            b = styrta.pop() 

            a = styrta.pop()
            if i == '*':

                styrta.append(a*b) 
            elif i == '-':
                styrta.append(a-b) 
            elif i == '+':

                styrta.append(a+b) 
            else:
                styrta.append(a//b)

    return styrta[0]
print(onp(['2', '1', '+', '3', '*'])) 
