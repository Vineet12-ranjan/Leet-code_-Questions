
import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        n = len(servers)
        
        free = [(servers[i], i) for i in range(n)]
        heapq.heapify(free)
        
        busy = []
        ans = []
        
        time = 0
        
        for j in range(len(tasks)):
            
            # Current time must never move backward
            time = max(time, j)
            
            # Release all available servers
            while busy and busy[0][0] <= time:
                available, weight, index = heapq.heappop(busy)
                heapq.heappush(free, (weight, index))
            
            # Wait if no server is free
            if not free:
                time = busy[0][0]
                
                while busy and busy[0][0] <= time:
                    available, weight, index = heapq.heappop(busy)
                    heapq.heappush(free, (weight, index))
            
            # Assign task to the best server
            weight, index = heapq.heappop(free)
            ans.append(index)
            
            # Update server's availability time
            heapq.heappush(
                busy,
                (time + tasks[j], weight, index)
            )
        
        return ans
