'''Run-Length Encoding:
Problem: Implement run-length encoding, a basic form of data
compression where consecutive occurrences of the same character are
replaced with the character followed by the number of occurrences.
o Example:
▪ Input: "aaabbc"
▪ Output: "a3b2c1"
Reference: GeeksforGeeks
'''

class Solution():
    def RunLengthEncoding (self, s):
        if not s:
            return ""
        
        encoded = ""
        count = 1
        # abbcd
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                encoded += s[i-1]+str(count)
                count = 1

        encoded += s[-1] + str(count)
        return encoded
    

s1 = Solution()
string = "aaabbc"
print(f"Original String : {string}")
print(f"Length Encoded String : {s1.RunLengthEncoding(string)}")