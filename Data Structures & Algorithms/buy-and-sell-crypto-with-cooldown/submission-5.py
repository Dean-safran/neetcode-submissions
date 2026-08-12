class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 2)]

        for i in range(len(prices) - 1, -1, -1) : 
            # if you can buy on day i
            cool_down = dp[i + 1][1]
            buy = -prices[i] + dp[i+1][0]
            dp[i][1] = max(cool_down, buy)

            # if you can't buy on day i
            cool_down = dp[i + 1][0]
            sell = prices[i] + dp[i+2][1]
            dp[i][0] = max(cool_down, sell)
        
        return dp[0][1]
        

