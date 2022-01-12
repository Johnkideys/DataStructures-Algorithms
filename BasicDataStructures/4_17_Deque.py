"""
The deque abstract data type is defined by the following
structure and operations. A deque is a structured and 
ordered collection of items where items are added and removed
from either end, either front or rear.
"""
# Rear > [ ............ ] < Front
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


d = Dequeue()

print(d.isEmpty())
d.addFront('rebeka')
d.addRear('elif')
d.removeFront()
d.addFront('has')
print(d.dequeue)

d.addFront('reb')
print(d.size)

print(d.dequeue)




