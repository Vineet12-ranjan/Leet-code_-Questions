 Maximum Nesting Depth of the Parentheses
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

 

class Solution:
    def maxDepth(self, s):
        depth = 0
        max_depth = 0

        for ch in s: 
            if ch == '(':
                depth += 1
                max_depth = max(max_depth, depth)

            elif ch == ')':
                depth -= 1

        return max_depth
