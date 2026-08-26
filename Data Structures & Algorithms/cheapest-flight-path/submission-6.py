import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """

        Use Bellman Ford alg

        """

        cost = [float('inf')] * n
        cost[src] = 0

        for _ in range(k + 1) : 
            tmp_cost = cost.copy()
            for edge in flights :
                curr, next, next_cost = edge
                if cost[curr] == float('inf') : 
                    continue
                if cost[curr] + next_cost < tmp_cost[next] :
                    tmp_cost[next] = cost[curr] + next_cost
            cost = tmp_cost


        if cost[dst] < float('inf') :
            return cost[dst]
        return -1
                
        



