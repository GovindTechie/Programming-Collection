def removeDuplicate(list2):
    removeList = []
    for elm in list2:
        if elm in removeList:
            continue
        else:
            removeList.append(elm)
    return removeList



list1 = [23, 66, 98, 24, 85, 2, 10, 98, 2]
print(f"Original list: {list1}")
print(f"Duplicate removed list: {removeDuplicate(list1)}")
