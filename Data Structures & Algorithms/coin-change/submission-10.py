class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp[x] is minimum number of coins needed to make amount x

        """    
        dp = {}
        dp[0] = 0

        for i in range(1, amount + 1) :
            possible_amounts = []
            for coin in coins :
                if coin > i :
                    continue
                if dp[i - coin] == float('inf') :
                    possible_amounts.append(float('inf'))
                else : 
                    possible_amounts.append(1 + dp[i - coin])
            if not possible_amounts :
                dp[i] = float('inf')
                continue
            dp[i] = min(possible_amounts)
        
        return -1 if dp[amount] == float('inf') else dp[amount]

                