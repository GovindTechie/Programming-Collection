class Solution(object):
    def lcmFind(self, num1, num2):
        small = num1 if num1<num2 else num2
        big = num1 if num1>num2 else num2
        i = 1
        d=1
        while(d):
            if((big*i)%small == 0):
                d = 0
                return big*i

s1 = Solution()
n1 = 4
n2 = 6
print(f"The original numbers are : {n1} and {n2}")
print(f"Lcm of two numbers is : {s1.lcmFind(n1, n2)}")