class Solution(object):
    def maxSlidingWindow(self, nums, k):
        result = []
        maxIndices = []
        for i in range(len(nums)):
            if(maxIndices and maxIndices[0] <= i-k):
                maxIndices.pop(0)
            
            while(maxIndices and nums[i] >= nums[maxIndices[-1]]):
                maxIndices.pop()
            
            maxIndices.append(i)

            if(i >= k-1) :
                result.append(nums[maxIndices[0]])

        return result


s1 = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(f"The original nums : {nums}\nValue of K : {k}")
print(f"The numbers after slideWindowMaximun : {s1.maxSlidingWindow(nums, k)}")
        