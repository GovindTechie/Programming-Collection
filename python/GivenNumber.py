def givenNumber(list2, n):
    present = False
    for ele in list2:
        if ele == n:
            present = True
    return present





list1 = [23, 53, 43, 58, 34, 22, 64 , 64, 43, 12]
n = 59
print(f"list: {list1}")
print(f"Number {n} in list: {givenNumber(list1, n)}")
