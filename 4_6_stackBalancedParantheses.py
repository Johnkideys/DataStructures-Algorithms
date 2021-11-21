
#The challenge then is to write an algorithm that will read a string of parentheses from left to right and decide whether the symbols are balanced.

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
    
str = '(()()(()))'
#str = '('
#str = '(())))'
#str = '(()))'
def isBalanced(str):
    s = Stack()
    balanced = True
    
    for i in str:
        # if i is equa to opening parantheses push it on to the stack
        if i == '(':
            s.push(i)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

    if balanced and s.isEmpty():
        return True
    else:
        return False

result = isBalanced(str)
print(f'str is a balanced parantheses: {result}')


