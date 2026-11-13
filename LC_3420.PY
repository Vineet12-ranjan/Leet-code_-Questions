
from collections import deque

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        dq = deque()
        right = n - 1
        cost = 0
        ans = 0

        for left in range(n - 1, -1, -1):
            x = nums[left]
            count = 1
            total = x

            while dq and dq[0][0] <= x:
                val, cnt, sm = dq.popleft()
                cost -= val * cnt - sm
                count += cnt
                total += sm

            dq.appendleft([x, count, total])
            cost += x * count - total

            while cost > k:
                val, cnt, sm = dq[-1]

                cost -= val - nums[right]

                dq[-1][1] -= 1
                dq[-1][2] -= nums[right]

                if dq[-1][1] == 0:
                    dq.pop()

                right -= 1

            ans += right - left + 1

        return ans
