def mergeList(list1, list2):
    return list1 + list2
    # list1.extend(list2)
    # return list1


list1 = [23, 53, 43, 58, 34, 22, 64 , 12]
list2 = [1, 5, 2, 9, 6]
print(f"Original list1: {list1}")
print(f"Original list2: {list2}")
print(f"Merged list: {mergeList(list1, list2)}")
