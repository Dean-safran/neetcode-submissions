class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        """

        you can either continue with the current coin, 
        or take the next coin

        recursively, you'd return 
        dp[i, amount] = min( 1 + helper(i, amount-coins[i]) , helper(i+1, amount) )

        """ 
        if amount == 0 :
            return 0

        dp = [[amount+1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp[len(coins)][0] = 0

        for i in range(len(coins) - 1, -1, -1) :
            for a in range(0, amount + 1) :
                if a - coins[i] < 0: 
                    dp[i][a] = dp[i+1][a]
                else : 
                    dp[i][a] = min(1 + dp[i][a-coins[i]], dp[i+1][a])
        if dp[0][amount] == amount+1 : 
            return -1
        return dp[0][amount]


        