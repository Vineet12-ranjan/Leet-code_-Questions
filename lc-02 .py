class Solution(object):
    def countGoodRotations(self, nums):
        n = len(nums)
        half = n // 2

        first = sum(nums[:half])
        second = sum(nums[half:])

        ans = 0

        for i in range(n):
            if first > second:
                ans += 1

            # Next rotation
            x = nums[i]
            y = nums[(i + half) % n]

            first = first - x + y
            second = second - y + x

        return ans





Q2. Count Good Cyclic Rotations
You are given an integer array nums of even length n.

A cyclic rotation of nums is obtained by choosing a prefix of nums whose length is between 0 and n - 1 (inclusive), and moving it to the end of the array while preserving the order of all elements.

A cyclic rotation is good if the sum of its first n / 2 elements is strictly greater than the sum of its last n / 2 elements.

Return the number of cyclic rotations of nums that are good.
