import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """

        could use dijkstra's where all points are connected to eachother

        """

        cost = dict()
        marg_cost = dict()
        visited = set()
        fringe = []

        tup_points = []
        for point in points : 
            tup_points.append(tuple(point))

        cost[tup_points[0]] = 0
        marg_cost[tup_points[0]] = 0
        heapq.heappush(fringe, (0, tup_points[0]))

        while fringe : 
            curr_cost, curr_point = heapq.heappop(fringe)
            if curr_point in visited :
                continue
            visited.add(curr_point)
            # update fringe point costs
            for point in tup_points : 
                if point in visited :
                    continue
                min_dist = abs(point[0] - curr_point[0]) + abs(point[1] - curr_point[1])
                if point not in marg_cost or marg_cost[point] > min_dist : 
                    marg_cost[point] = min_dist
                    heapq.heappush(fringe, (marg_cost[point], point))
                
        min_cost = 0
        for point in marg_cost : 
            min_cost += marg_cost[point]
        return min_cost
                