'''Encoding Strings with Custom Rules:
Problem: Given a string, encode it by replacing each character with its
corresponding position in the alphabet (e.g., 'a' = 1, 'b' = 2, ..., 'z' = 26).
Then, concatenate these numbers to form the encoded string.
Example:
▪ Input: "abc"
▪ Output: "123"
Reference: PrepInsta 
'''

class Solution():
    def encodeString(self, s):
        return "".join(f"{ord(i)-ord('a')+1:02d}" for i in s if 'a' <= i <= 'z') 
        # we seperate the number using space as it is able to currectly decode the string
        # example to avoid confusion as 2426 -> xy or bdbe 

s1 = Solution()
string = "hello"
print(f"Original String : {string}")
print(f"Encoded string : {s1.encodeString(string)}")


