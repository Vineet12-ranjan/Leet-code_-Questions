class Solution(object):
    def minSwaps(self, nums):
        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            
            return total
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        index_map = {num: i for i, num in enumerate(nums)}
        swaps = 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                swaps +=1
                j = index_map[sorted_nums[i]]
                index_map[nums[i]] = j
                index_map[sorted_nums[i]] = i

                nums[i], nums[j] = nums[j], nums[i]

        return swaps           
