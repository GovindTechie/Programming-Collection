# def listLenght(list2):
#     return len(list2)



def listLength(list2):
    lenght = 0 
    for ele in list2:
        lenght += 1
    return lenght



list1 = [23, 53, 43, 58, 34, 22, 64 , 64, 43, 12]
print(f"list: {list1}")
print(f"length of list: {listLength(list1)}")
