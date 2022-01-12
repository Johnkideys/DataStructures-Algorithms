import random

class PrintQueue:
    def __init__(self):
        self.tasks = []
    
    def isEmpty(self):
        return self.tasks == []

    def enqueue(self, item):
        self.tasks.insert(0,item)
    
    def dequeue(self):
        return self.tasks.pop()
    
    def size(self):
        return len(self.tasks)

class Students:
    def __init__(self, num):
        self.newTask = num # an integer, rasndom num of pages to print

#x1 = Students(5)
#print(x1.newTask)

def generateRandom():
    currentSec = random.randrange(1,180)
    return currentSec


def runSimulation(totalSec):
    curSec = generateRandom()

    if curSec == 180:
        pass




