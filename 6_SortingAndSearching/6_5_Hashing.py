
# Implementing the Map Abstract Datatype

# use two lists to create a HashTable class that implements 
# the Map abstract data type


class HashTable:
    def __init__(self) -> None:
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    # hash_function >> simple remainder method
    def hash_function(self, key, size):
        return key%size


    # collision resolution technique is linear probing 
    # with a “plus 1” rehash function
    def put(self, key, data):
        hash_value = self.hash_function(key, self.size)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data # replace 
            else:
                nextslot = self.rehash(hash_value, self.size)
                while self.slots[nextslot] != None and \
                      self.slots[nextslot] != key:

                    nextslot = self.rehash(hash_value, self.size)

                # below if-else is out of while loop !    
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data # replace
    def get(self,key):
        startslot = self.hash_function(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                            not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data



    def rehash(self, old_hash_value, size):
        return (old_hash_value+1) % size
    
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


x = HashTable()
x[0]='12'
x[56] = 567
x[3] = 45
x[36] = 89
#x[47] = 89



print(x[0])
print(x[56])
#print(x.__getitem__(0))

print(x.slots)
print(x.data)

