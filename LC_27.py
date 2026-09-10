class Solution:
    def removeElement(self, num, val):
        i = 0
        j = len(num) - 1

        while i <= j:
            if num[i] == val:
                num[i] = num[j] 
                j -= 1
            else:
                i += 1

        return j + 1        
