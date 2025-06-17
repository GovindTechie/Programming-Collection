'''Check for Anagrams:
Problem: Write a function to determine if two given strings are anagrams
of each other.
Example:
▪ Input: "listen", "silent"
▪ Output: True
'''



# # approach 1
# from collections import Counter
# def checkAnagrams(sting1, string2):
#     dect1 = Counter(string1)
#     dect2 = Counter(string2)

#     if dect1 == dect2:
#         return True
#     else :
#         return False


# approach 2
def checkAnagrams(string1, string2):
    return sorted(string1) == sorted(string2)
        


string1 = "listen"
string2 = "silent"
print(f"String one is : {string1}\n String two is : {string2}")
print(f"Is both string are anagrams : {checkAnagrams(string1, string2)}")
