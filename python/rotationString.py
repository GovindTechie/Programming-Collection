'''
Check If One String is a Rotaon of Another
Example
Input: "waterbole", "erbolewat"
Output: True
'''

def is_rotation(a, b):
    if len(a) != len(b):
        return False
    return b in (a + a)


str1 = "waterbole"
str2 = "erbolewat"

print(f"Original strings are : {str1}, {str2}")
print(f"is rotation : {is_rotation(str1, str2)}")