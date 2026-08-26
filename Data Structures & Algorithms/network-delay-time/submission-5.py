from collections import deque
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost = dict()
        visited = set()
        cost[k] = 0
        fringe = []
        heapq.heappush(fringe, (0, k))

        # make adj list
        adj_list = dict()
        for edge in times : 
            if adj_list.get(edge[0]) : 
                adj_list.get(edge[0]).append((edge[1], edge[2]))
            else : 
                adj_list[edge[0]] = [(edge[1], edge[2])]
        
        while fringe :
            curr_cost, curr = heapq.heappop(fringe)
            if curr in visited :
                continue
            visited.add(curr)
            if curr not in adj_list :
                continue
            for edge in adj_list[curr] :
                next = edge[0]
                next_cost = edge[1]
                if next in visited :
                    continue
                if next not in cost or (cost[curr] + next_cost) < cost[next] : 
                    cost[next] = curr_cost + next_cost
                    heapq.heappush(fringe, (cost[next], next))

        if len(cost) < n :
            return -1

        max = -1
        for node in cost :
            if cost[node] > max : 
                max = cost[node]
        return max
        
        
                    