class Solution(object):
    def reverse(self, x):
        INT_MIN = -2**31      # -2147483648
        INT_MAX = 2**31 - 1   # 2147483647

        sign = -1 if x < 0 else 1   # Save the sign
        x = abs(x)                  # Work with positive value
        rev = 0

        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        rev = rev * sign

        # Check 32-bit range
        if rev < INT_MIN or rev > INT_MAX:
            return 0

        return rev
