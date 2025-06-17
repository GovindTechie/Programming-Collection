class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1]*n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
            

        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
        

s1 = Solution()
nums = [1,2,3,4]
print(f"Numbers are : {nums}")
print(f"Product ExceptSelf : {s1.productExceptSelf(nums)}")
