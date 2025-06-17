'''this is a function that reverses a string.
Input : “Geeks”
Output “skeeG"
'''


# approach 1
def reverse(string):
    reversed_string = string[::-1]
    return reversed_string

# # approach 2
# def reverse(string):
#     l = list(string)
#     l.reverse()
#     string1 = "".join(l)
#     return string1
    

# # approach 3
# def reverse(s):
#     reverseString = ""
#     for i in range(len(s)-1, -1, -1):
#         reverseString += s[i]
#     return reverseString


string = "Geeks"
print(f"Orginal String : {string}")
print(f"Reversed String : {reverse(string)}")
