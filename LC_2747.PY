
class Solution(object):
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        q = sorted((t, i) for i, t in enumerate(queries))

        count = {}
        left = 0
        right = 0
        result = [0] * len(queries)

        for t, idx in q:
            while right < len(logs) and logs[right][1] <= t:
                server = logs[right][0]
                count[server] = count.get(server, 0) + 1
                right += 1

            while left < right and logs[left][1] < t - x:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            result[idx] = n - len(count)

        return result
