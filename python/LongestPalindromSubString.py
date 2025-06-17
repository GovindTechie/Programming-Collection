'''Find the Longest Palindromic Substring:
Problem: Given a string, find the longest substring that is a palindrome.
Example:
▪ Input: "babad"
▪ Output: "bab"
''' 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""

        for i in range(len(s)):
            odd_palindrome = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            even_palindrome = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest

# Test cases
s1 = Solution()
print(s1.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(s1.longestPalindrome("cbbd"))   # Output: "bb"
print(s1.longestPalindrome("a"))      # Output: "a"
print(s1.longestPalindrome("ac"))     # Output: "a" or "c"
