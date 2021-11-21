# One of the typical applications for showing a queue
# in action is to simulate a real situation that requires
#  data to be managed in a FIFO manner. Hot Potato Game:


class Queue:
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return self.qlist == []

    def enqueue(self, item):
        self.qlist.insert(0, item)

    def dequeue(self):
        return self.qlist.pop()
    
    def size(self):
        return len(self.qlist)

    def lastItem(self):
        return self.qlist[-1]

que = Queue()

#create the queue

name = input('give a name to add to the queue: ')
while name != '0':
    que.enqueue(name)
    name = input('give a name for the queue: ')

#print the queueu to visualize
print(que.qlist)

def HotPotato(num,que):
    another_cycle = num
    while que.size() != 1:
        for i in range(num):
            putBack = que.dequeue()
            que.enqueue(putBack)        
        que.qlist.pop()
        num = another_cycle
    return que.qlist[0]

answer = HotPotato(7,que)
print(answer)




