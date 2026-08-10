class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * 2
        
        for i in range(n) :
            dp[0][i] = 1
        
        for i in range(m - 1) :
            for j in range(n) :
                temp = 0
                if j - 1 >= 0 :
                    temp += dp[0][j - 1]
                temp += dp[0][j]
                dp[1][j] = temp
            for i in range(n) :
                dp[0][i] = dp[1][i]
        return dp[0][n-1]