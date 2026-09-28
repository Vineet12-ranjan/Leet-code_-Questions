class Solution:
    def reverse(self, x):
        negative = x < 0
        x = abs(x)

        rev = 0

        while x > 0:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit

        if negative:
            rev = -rev

        if rev < -2147483648 or rev > 2147483647:
            return 0

        return rev
