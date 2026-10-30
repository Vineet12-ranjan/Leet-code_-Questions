
import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        pq = [(0, 0, 1)]
        dist = {}

        while pq:
            cost, node, count = heapq.heappop(pq)

            if node == n - 1:
                return cost

            if (node, count) in dist and dist[(node, count)] <= cost:
                continue

            dist[(node, count)] = cost

            for nxt, weight in graph[node]:
                if labels[nxt] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count <= k:
                    new_cost = cost + weight
                    state = (nxt, new_count)

                    if state not in dist or new_cost < dist[state]:
                        heapq.heappush(
                            pq, (new_cost, nxt, new_count)
                        )

        return -1
