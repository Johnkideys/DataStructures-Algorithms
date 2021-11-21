# create a new class for the implementation of the abstract data type queue.

# decide which end of the list to use as the rear and which to use as the front.
# assume that the rear is at position 0 in the list 
# This allows us to use the insert function on lists to add new elements to the rear of the queue. The pop operation can be used to remove the front element (the last element of the list).
# Recall that this also means that enqueue will be O(n) and dequeue will be O(1).
#FIFO

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

x = Queue()
print(x.isEmpty())
x.enqueue(5)
x.enqueue('4')
x.enqueue(6)
print(x.size())
print(x.dequeue())

for i in x.items:
    print(type(i))










