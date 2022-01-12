#Use Deque to check if a string is a palindrome

class Dequeue:
    def __init__(self):
        self.dequeue = []

    def addFront(self, item):
        self.dequeue.append(item)
    
    def addRear(self, item):
        self.dequeue.insert(0, item)
    
    def removeFront(self):
        return self.dequeue.pop()
    
    def removeRear(self):
        return self.dequeue.pop(0) # will pop the item at index 0
    
    def isEmpty(self):
        return self.dequeue == []
    
    def size(self):
        return len(self.dequeue)


word = input('Enter a word and I will check whether it is a palindrome or not!: ')

dq = Dequeue()

for i in word:
    dq.addRear(i)

checkEven = 'pal'
while dq.size() > 1: 
    if dq.size() % 2 == 0:
        if dq.removeFront() != dq.removeRear():
            checkEven = 'notpal'
    if dq.size() % 2 == 1 and dq.size() > 1:
        if dq.removeFront() != dq.removeRear():
            checkEven = 'notpal'

if checkEven == 'pal':
    print('palindrome')
else:
    print('not palindrome!')
    
   

        
