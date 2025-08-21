class Solution(object):
    def processStr(self, s):
        result = ""
        for ch in s:
            if(ord(ch) >= 97 and ord(ch) <= 122):
                result+=ch
            if(ch == '*' and len(result) != 0):
                result = result[:-1]
            if(ch == '#' and len(result) != 0):
                result += result
            if(ch == '%' and len(result) > 1):
                result = result[::-1] 
        return result
      
s1 = Solution()
s = "a#b%*"
print(f"Original String : {s}")
print(f"After Processing String : {s1.processStr(s)}")