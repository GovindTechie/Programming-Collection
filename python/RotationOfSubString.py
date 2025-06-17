'''
Check if a string S1 is a rotation of string S2.
Input: S1 = "abcde", S2 = "cdeab"
Output: True
'''

def rotationOfSubtringCheck(s1, s2):
    if(len(s1) != len(s2)):
        return False
    return s2 in (s1+s1)



s1 = "abcde"
s2 = 'cdeab'
print(f"Strings are {s1}, {s2}")
print(f"Rotation of substring {rotationOfSubtringCheck(s1, s2)}")