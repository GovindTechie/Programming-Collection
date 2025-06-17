'''
Maximum Subarray Sum (Standard Kadane’s Algorithm)
Problem Statement:
Given an integer array nums, find the conguous subarray (containing at
least one number)
which has the largest sum and return its sum.
Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanaon: The subarray [4,-1,2,1] has the maximum sum = 6.
'''


def max_subarray_sum (nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum+num)
        max_sum = max(max_sum, current_sum)

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))  