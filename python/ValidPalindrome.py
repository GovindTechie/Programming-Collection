# # by using isalnum without re
# class Solution(object):
#     def isPalindrome(self, s):
#         s = s.lower()
#         cleaned = ""
#         for char in s:
#             if char.isalnum():
#                 cleaned += char
#         return(cleaned == cleaned[::-1])
    

# by using re
import re
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        return(s == s[::-1])
          


s1 = Solution()
s = "A man, a plan, a canal: Panama"
print(f"Original String is : {s}")
print(f"Is string is palindrome : {s1.isPalindrome(s)}")
