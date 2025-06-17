'''Permutations of given String
Input: s = “ABC”
Output: “ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”
'''


# # approach 1
# from itertools import permutations
# def permutationOfString(s):
#     print(["".join(p) for p in permutations(s)])



# approch 2
def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    
    for i in range(len(s)):
        ch = s[i]  
        remaining = s[:i] + s[i+1:]  
        permute(remaining, answer + ch)  



string = "ABC"
print(f"String is : {string}")
permute(string)


