wyr = [3,7,'+',2,3,'+','-']

def reverse_polish_notation(wyr):
    stack = []
    for elem in wyr:
        if type(elem) == int:
            stack.append(elem)
        if type(elem) == str:
            a, b = str(stack[-2]), str(stack[-1])
            stack = stack[:len(stack)-2]
            stack.append(eval(a+elem+b))
    if len(stack) == 1:
        return stack[0]
    else:
        return 'error'

print(reverse_polish_notation(wyr))
            
            
