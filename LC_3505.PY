class Solution(object):
    def minOperations(self, nums, x, k):

        n = len(nums)

        if n < x * k:
            return -1

        vals = sorted(set(nums))
        m = len(vals)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit_count = [0] * (m + 1)
        bit_sum = [0] * (m + 1)

        def update(bit, i, value):
            while i <= m:
                bit[i] += value
                i += i & -i

        def query(bit, i):
            result = 0
            while i > 0:
                result += bit[i]
                i -= i & -i
            return result

        def kth(kth_value):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and bit_count[nxt] < kth_value:
                    idx = nxt
                    kth_value -= bit_count[nxt]
                step >>= 1

            return idx + 1

        def add(v, delta):
            r = rank[v]
            update(bit_count, r, delta)
            update(bit_sum, r, v * delta)

        def get_cost():
            mid = kth((x + 1) // 2)
            median = vals[mid - 1]

            left_count = query(bit_count, mid)
            left_sum = query(bit_sum, mid)

            total_sum = query(bit_sum, m)
            total_count = query(bit_count, m)

            right_count = total_count - left_count
            right_sum = total_sum - left_sum

            return (median * left_count - left_sum +
                    right_sum - median * right_count)

        costs = []

        for i in range(n):
            add(nums[i], 1)

            if i >= x:
                add(nums[i - x], -1)

            if i >= x - 1:
                costs.append(get_cost())

        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):

            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                curr[i] = curr[i - 1]

                if i >= x and prev[i - x] != INF:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
