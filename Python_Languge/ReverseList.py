# def reverseList(list2):
#     lenght = len(list2)
#     for i in range(0, lenght//2):
#         temp = list2[i]
#         list2[i] = list2[lenght-1-i]
#         list2[lenght-1-i] = temp

#     return list2

# def reverseList(list2):
#     reversed_list = list2[::-1]
#     return reversed_list

def reverseList(list2) :
    list2.reverse()
    return list2



list1 = [23, 53, 58, 34, 64 , 43, 12]
print(f"Original list: {list1}")
print(f"Reversed list: {reverseList(list1)}")
