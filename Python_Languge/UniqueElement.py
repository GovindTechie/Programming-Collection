def uniqueElement(list2):
    UniqueList = []
    notUnique = set()
    for elm in list2:
        if elm in UniqueList or elm in notUnique:
            UniqueList.remove(elm)
            notUnique.add(elm)
        else:
            UniqueList.append(elm)
    return UniqueList



list1 = [23, 53, 43, 58, 34, 22, 64 , 64, 43, 12]
print(f"Original list: {list1}")
print(f"Unique elements: {uniqueElement(list1)}")