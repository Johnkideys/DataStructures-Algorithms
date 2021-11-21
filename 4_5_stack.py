"""
 in Python, as in any object-oriented programming language, the implementation of choice for an abstract data type such as a stack is the creation of a new class. The stack operations are implemented as methods.
 """

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self): #returns top item from the stack but doesnt remove it
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

x = Stack()

print(x.isEmpty())
x.push('tennis')
x.push(4)
print(x.isEmpty())
print(x.peek())
print(x.pop())
print(x.peek())
print(x.pop())
print(x.isEmpty())




