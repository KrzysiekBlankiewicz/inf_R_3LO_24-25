class Stack:
    def __init__(self,value=None):
        self.size = 0
        self.item = []
        if value != None:
            self.push(value)
            
    def empty(self):
        if self.size == 0:
            return True
        else:
            return False
        
    def pop(self):
        if not self.empty():
            self.size -= 1
            return self.item.pop()
        
    def push(self, value):
        self.size += 1
        self.items.append(value)
        
    def peek(self):
        return self.items[-1]

st=(4,6,7,4)
print(Stack.empty(st))
