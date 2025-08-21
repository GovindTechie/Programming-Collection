class Solution(object):
    def myPow(self, x, n):
        result = 1
        for i in range(abs(n)):
            result *= (1/x)
        return result

    
        
s1 = Solution()
x = 2.00000
n = -2
print(f"Orginial expresion : {x}^{n}")
print(f"The answer is : {s1.myPow(x, n)}")