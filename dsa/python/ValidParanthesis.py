class Solution(object):
    def isValid(self, s):
        stack = []
        pairBrackt = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for ch in s:
            if(ch == '(' or ch == '[' or ch == '{'):
                stack.append(ch)
            else :
                if(not stack or stack[-1] != pairBrackt[ch]):
                    return False
                stack.pop()
        
        return not stack

            
        

s1 = Solution()
s = "()[]{}"
print(f"The string is : {s}")
print(f"Is string parenthesis matching {s1.isValid(s)}")
