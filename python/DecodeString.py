'''Decoding Numeric Strings to Text:
Problem: Given a numeric string where each pair of digits represents a
letter ('01' = 'a', '02' = 'b', ..., '26' = 'z'), decode the string into its
corresponding text.
Example:
▪ Input: "08151212"
▪ Output: "hello"
Reference: PrepInsta 
'''
class Solution():
    def decodeString(self, s):
        splitList = [int(s[num:num+2]) for num in range (0, len(s), 2)]
        
        return "".join(chr(int(num)+ord('a')-1) for num in splitList)



s1 = Solution()
string = "0805121215"
print(f"Original String: {string}")
print(f"Encoded String: {s1.decodeString(string)}")

