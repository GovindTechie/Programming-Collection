#  in this problem we have to find longest substring such that no element in it repeating

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1  

            charSet.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

# Test case
s1 = Solution()
print(s1.lengthOfLongestSubstring("abcb"))  # Expected Output: 3
