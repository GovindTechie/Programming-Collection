friends = ["Apple", "Veer", "Raj", True, 9]
print(friends)


friends.append("Atharv")
print(friends)

l1 = [3,6,1,9,2,5,2,6,43,0,6]
print(l1.index(6))
print(l1*2)
l1.sort()
l1.reverse()
print(l1)

l1.insert(1, 25)
print(l1)

print(l1.pop(0))
print(l1)

l1.remove(25)
print(l1)


New_list = friends.copy()
print(f"New list is : {New_list} ")

# friends = ["Apple", "Veer", "Raj", True, 9]
# friends[0][2] = 'd'
# print(friends)

#  Traceback (most recent call last):
#   File "D:\Python\NLP_ISE\list.py", line 22, in <module>
#     friends[0][2] = 'd'
#     ~~~~~~~~~~^^^
# TypeError: 'str' object does not support item assignment

