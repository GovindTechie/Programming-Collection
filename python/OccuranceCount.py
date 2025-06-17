from collections import Counter
def occuranceCount(list2):
    dict1 = dict(Counter(list2))
    return dict1




list1 = [23, 53, 43, 58, 34, 22, 64 , 64, 43, 12]
print(f"list: {list1}")
print(f"Occurance: {occuranceCount(list1)}")
