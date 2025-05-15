'''Next Permutaon (Amazon, Google, Microsoft)
Given an array of numbers, find the next lexicographically greater
permutaon.
'''


def next_permutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1:] = reversed(nums[i + 1:])
    return nums


nums = [1, 2, 3]
print(f"Original Numbers : {nums}")
print(f"Permutaions : {next_permutation(nums)}")