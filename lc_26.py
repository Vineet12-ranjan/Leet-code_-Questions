class Solution(object):
    def removeDuplicates(self, num):
        if not num:
            return 0
        
        k = 1
        for i in range(1, len(nums)):
            if num[i] != num[i - 1]:
                num[k] = num[i]
                k += 1


        return k        
