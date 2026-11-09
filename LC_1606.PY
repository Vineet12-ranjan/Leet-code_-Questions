
from sortedcontainers import SortedList
import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):
        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                end_time, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            server = available.bisect_left(i % k)

            if server == len(available):
                server = 0

            assigned = available.pop(server)

            count[assigned] += 1

            heapq.heappush(
                busy,
                (arrival[i] + load[i], assigned)
            )

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
