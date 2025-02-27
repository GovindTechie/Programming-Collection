
'''Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

class Solution():
    def isValid(self, s):
        """
        :type s:str
        :rtype:bool
        """
        seen = []
        bracket_map = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in bracket_map.values():
                seen.append(char)

            else:
                if not seen or seen[-1] != bracket_map[char]:
                    return False
                seen.pop()

        return len(seen) == 0

                




s1 = Solution()
print(s1.isValid("()[]{}"))  # ✅ Output: True
print(s1.isValid("(]"))      # ✅ Output: False
print(s1.isValid("([{}])"))  # ✅ Output: True
print(s1.isValid("({[)]}"))  # ✅ Output: False
