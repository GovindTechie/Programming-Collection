'''Caesar Cipher Encryption:
Problem: Implement the Caesar Cipher encryption technique, which
shifts each letter in the plaintext by a fixed number of positions down the
alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E',
and so on. Wrap around to the beginning of the alphabet if necessary.
Example:
▪ Input: "HELLO", Shift: 3
▪ Output: "KHOOR"
Reference: Scribd 
'''

class Solution():
    def CaesarCipherEncryption(self, s):
        return ("".join(chr(ord(char)+3) for char in s))


s1 = Solution()
string = "HELLO"
print(f"Original String is : {string}")
print(f'After CaesarCipherEncryption : {s1.CaesarCipherEncryption(string)}')
