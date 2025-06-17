'''
You are given two strings A and B. Create a new password by alternang
characters from
A and B. If one string is shorter, append the remaining characters of the
longer string at the end.

Sample Input:
abc
xyzpq
Sample Output:
Axbyczpq
'''

def newPassword(s1, s2):
    result = []
    len1, len2 = len(s1), len(s2)

    for i in range(min(len1, len2)):
        result.append(s1[i])
        result.append(s2[i])

    result.append(s1[i+1:] if len1 > len2 else s2[i+1:])

    return "".join(result)



s1 = "abc"
s2 = "xyzpq"
print(f"Orgininal list are {s1} and {s2}")
print(f"New Password is : {newPassword(s1, s2)}")