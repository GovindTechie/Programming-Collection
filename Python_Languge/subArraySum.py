'''
Subarray Sum Equals K
Find the number of connuous subarrays that sum up to k.
Example:
Input: nums = [1,1,1], k = 2
Output: 2
'''

def subArraySum(arr, k):
    count = 0
    for i in range(0, len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == k:
                count += 1
    return count



arr = [1,1,1]
k = 2
print(f"Original array is : {arr}")
print(f"Sub arrays count of sum = k : {subArraySum(arr, k)}")


