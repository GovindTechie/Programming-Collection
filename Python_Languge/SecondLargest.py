def SecondLargest(list2):
    nums = list(set(list2))  
    nums.sort(reverse=True)  
    return nums[1] 




list1 = [23, 53, 43, 58, 34, 22, 64 , 64, 43, 12]
print(f"list: {list1}")
print(f"Secnod largest in list is : {SecondLargest(list1)}")