class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1

s1 = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(f"The numbers are : {nums}\nTarget : {target}")
print(f"Index of target : {s1.search(nums, target)}")

