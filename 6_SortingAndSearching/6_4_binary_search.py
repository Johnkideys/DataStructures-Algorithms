# find 3 and 13 in the below list
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]

def binary_search(list1, item):
   
       while True:
        middle = len(list1)//2
        mid_num = list1[middle]
        

        if item == mid_num:
            return True
        elif item < mid_num and len(list1) > 2:
            list1 = list1[0:middle]
        elif item > mid_num and len(list1) > 2:
            list1 = list1[(middle+1)::]
        else:
            for i in list1:
                if i == item:
                    return True
                else:
                    return False
        
result = binary_search(testlist, 43)
print(result)