''' Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''

# The following approach is very better approach as it just taking O(n) time complexity 
from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False  # s1 is longer than s2, so impossible.

        s1_count = Counter(s1)  # Frequency of s1
        window_count = Counter(s2[:len_s1])  # First window of s2

        if s1_count == window_count:
            return True  # First window is already a match

        for i in range(len_s1, len_s2):
            window_count[s2[i]] += 1  # Add new char to the window
            window_count[s2[i - len_s1]] -= 1  # Remove the oldest char

            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]  # Remove zero-count chars

            if window_count == s1_count:
                return True  # Found a valid permutation

        return False  # No permutation found


s1 = Solution()
print(f"The s1 strings one or more permutations present in s2 : "
      f"{s1.checkInclusion("afdgdgfhgfgefgfdgdfhb", "afdgdgfhgfgefgfdgdfhb")}")








'''This approch is not good as it taking O(n!) time complexity 
If s1 = "abcdef", you generate 720 (6!) permutations!
If s1 = "abcdefgh", you generate 40,320 (8!) permutations!
'''

# from itertools import permutations
# def permutationOfString(s):
#     list1 = ["".join(p) for p in permutations(s)]
#     return list1

# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         s1Permutation = permutationOfString(s1)
#         for perm in s1Permutation:
#             if perm in s2:
#                 return True
#         return False
        