class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if(nums[mid] == target):
                return mid
            

            # check if left half is sorted
            if(nums[left] <= nums[mid]):
                if(nums[left] <= target < nums[mid]):
                    right = mid -1
                else :
                    left = mid + 1
            
            else:
                # right half is sorted
                if(nums[mid] < target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

s1 = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(f"Array : {nums}\nTarget : {target}")
print(f"The index of target : {s1.search(nums, target)}")

