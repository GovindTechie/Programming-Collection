#  Find Duplicates from given list [2,5,8,4,5,2,3,8,4,6,10,25]

list1 = [2, 5, 8, 4, 5, 2, 3, 8, 4, 6, 10, 25]

seen = set()
duplicates = list()

for num in list1:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)

print(f"Duplicates : {list(duplicates)}")