# [1,23,45,67,9]

def seq_search(list1, item):
    found = 0
    for i in list1:
        if i == item:
            found=1
            return True
    return False

def seq_search_while_loop(list1, item):
    found = 0
    pos = 0
    while pos < len(list1) and found==0:
        if list1[pos] == item:
            found=1
        else:
            pos += 1
    return bool(found)




list_nums = [1,23,45,67,9]
print(seq_search(list_nums, 9))

print(seq_search_while_loop(list_nums, 9))