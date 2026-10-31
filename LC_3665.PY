
class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):

                if dp[i][j] == 0:
                    continue

                ways = dp[i][j]

                # Move right
                if j + 1 < n:
                    x, y = i, j + 1

                    while x < m and y < n and grid[x][y] == 1:
                        x += 1

                    if x < m and y < n:
                        dp[x][y] = (dp[x][y] + ways) % MOD

                # Move down
                if i + 1 < m:
                    x, y = i + 1, j

                    while x < m and y < n and grid[x][y] == 1:
                        y += 1

                    if x < m and y < n:
                        dp[x][y] = (dp[x][y] + ways) % MOD

        return dp[m - 1][n - 1]
