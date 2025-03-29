'''
Find All Subsequences of a String (Goldman Sachs, PayPal)
s = "abc"
Output
["", "a", "b", "c", "ab", "ac", "bc", "abc"]
Hint: Use Recursion.'
'''


def SubSequence(s):
    if not s:
        return [""]
    smaller_subsequences = SubSequence(s[1:]) 
    return smaller_subsequences + [s[0] + sub for sub in smaller_subsequences]
   



string = "abc"

print(f"Original String : {string} ")
print(f"Subsequence of String : {SubSequence(string) }")