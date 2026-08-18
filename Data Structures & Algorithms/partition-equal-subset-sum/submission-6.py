class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """

        can either include or exclude an element in the current set 



        """

        if len(nums) < 2 :
            return False 

        def sum(l) : 
            res = 0
            for i in range(len(l)) : 
                res += l[i]
            return res

        total = sum(nums)
        if total % 2 != 0 :
            return False 
        total = total // 2

        dp = [[False for _ in range(total+1)] for _ in range(len(nums)+1)]

        for i in range(0, len(nums) + 1) : 
            dp[i][total] = True

        for i in range(len(nums) - 1, -1, -1) :
            for c in range(0, total) :
                if dp[i+1][c] :
                    dp[i][c] = True
                elif c + nums[i] <= total : 
                    dp[i][c] = dp[i+1][c + nums[i]]
        return dp[0][0]



