
#Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

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

def revstring(mystr):
    revstr = ''

    rev = Stack()
    for i in mystr:
        rev.push(i)
    while rev.isEmpty() == False:
        revstr = revstr + rev.pop() 
    
    return revstr

result = revstring('climate')
print(result)