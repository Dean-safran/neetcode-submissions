class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1 = cost[0]
        dp2 = cost[1]

        for i in range(2, len(cost)) :
            temp = min(dp1, dp2) + cost[i]
            dp1 = dp2
            dp2 = temp
        return min(dp1, dp2)