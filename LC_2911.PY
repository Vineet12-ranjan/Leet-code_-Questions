
class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        INF = float('inf')

        # Step 1: Precompute minimum changes
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for length in range(2, n - i + 1):
                j = i + length - 1

                # Try every proper divisor
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Check each group
                    for r in range(d):
                        left = i + r
                        right = i + r + ((length - 1 - r) // d) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        # Step 2: Dynamic Programming
        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):

                    if dp[start][parts - 1] == INF:
                        continue

                    dp[end][parts] = min(
                        dp[end][parts],
                        dp[start][parts - 1] + cost[start][end - 1]
                    )

        return dp[n][k]
