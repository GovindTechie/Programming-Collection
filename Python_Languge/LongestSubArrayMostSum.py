'''
Longest Subarray with Sum at Most K
Input: nums = [3, 1, 2, 7, 4, 2, 1], K = 8
ISE Component Name Marks Applicable CO
1 Coding Assignment 10 CO3
Output: 4
Explanaon: The subarray [3,1,2,2] has sum ≤ 8
'''


def LongestSubstring (nums, k) :
    left = 0
    current_sum = 0
    max_length = 0


    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > k:
            current_sum -= nums[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


nums = [3, 1, 2, 7, 4, 2, 1]
K = 8
print(f"Original numbers : {nums} ")
print(f"Longest Substring {LongestSubstring(nums, K)} ")

