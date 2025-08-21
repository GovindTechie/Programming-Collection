class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        i = 5
        while(n // i > 0):
            count += n//i
            i *= 5
        return count
    
s1 = Solution()
n = 5
print(f"The number is : {n}")
print(f"The TrailingZeroes in Factorial : {s1.trailingZeroes(n)}")
