class Solution(object):
    def plusOne(self, digits):
        # value = 0
        # rem = 1
        # for i in range(len(digits)):
            
        #     value += rem*digits[len(digits)-1-i]
        #     rem *= 10
        
        # value += 1
        # ans = [int(digit) for digit in str(value)]
        # return ans
    
        # simple approach
        n = len(digits)
        for i in reversed(range(n)):
            if(digits[i]<9):
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

        
        
s1 = Solution()
digits = [4,3,2,1]
print(f"Original list is {digits}")
print(f"after adding one {s1.plusOne(digits)}")