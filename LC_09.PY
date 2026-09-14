class Solution:
    def isPalindrome(self, x):

        if x < 0:
            return False

        s = str(x)

        return s == s[::-1]




9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.


