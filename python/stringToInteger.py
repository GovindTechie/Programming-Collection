class Solution(object):
    def myAtoi(self, s):

        # removing space at starting 
        i = 0
        while i<len(s) and s[i] == " ":
            i+=1
        s = s[i:]

        i = 0
        if not s:
            return 0
        
        # sign checking
        sign = 1
        if s[i] == '+':
            sign = 1
            i+=1
        elif s[i] == '-':
            sign = -1
            i+=1

        # is digit checking 
        result = ""
        while i < len(s) and (s[i].isdigit()):
            result += s[i]
            i+=1
        
        if result == "":
            return 0
        result = int(result)

        # return process
        MAX_INT = 2**31-1
        MIN_INT = -2**31
        
        if sign == 1:
            return min(result, MAX_INT)
        else :
            return max(-result, MIN_INT)

s1 = Solution()
str = "42"
print(f"Original String is : {str}")
print(f"After converting string to integer : {s1.myAtoi(str)}")