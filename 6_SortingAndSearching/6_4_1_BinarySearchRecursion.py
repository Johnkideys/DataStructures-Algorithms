
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]

def binary_with_recursion(list1, item):
    if len(list1) == 0:
        return False
    else:
        mid = len(list1)//2

        if item==list1[mid]:
            return True
        elif item < list1[mid]:
            list1 = list1[:mid]
        else:
            list1 = list1[(mid+1):]
        
        return binary_with_recursion(list1, item)

result = binary_with_recursion(testlist, 42)
print(result)