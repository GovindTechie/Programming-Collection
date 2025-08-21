class Solution(object):
    def primeCheck(self, n):
        if(n<=1):
            return False
        for i in range(2, int(n**0.5)) :
            if(n%i == 0) :
                return False
        return True
    
s1 = Solution()
n = 2
print(f"The number is : {n}")
print(f"is it prime : {s1.primeCheck(n)}")
