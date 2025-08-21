class Solution(object):
    def gcdFind(self, num1, num2):
        while num2:
            num1, num2 = num2, num1%num2
        return num1

s1 = Solution()
n1 = 78
n2 = 52
print(f"The original numbers are : {n1} and {n2}")
print(f"Gcd of two numbers is : {s1.gcdFind(n1, n2)}")