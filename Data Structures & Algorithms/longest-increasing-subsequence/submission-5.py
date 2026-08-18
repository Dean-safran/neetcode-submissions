class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))] 

        if len(nums) == 1 : 
            return 1
        dp[0] = 1

        for i in range(1, len(nums)) : 
            max = 0
            for j in range(0, i) :
                if nums[i] > nums[j] :
                    if dp[j] > max :
                        max = dp[j]
            dp[i] = 1 + max

        res = 0
        for i in range(len(dp)) : 
            if dp[i] > res :
                res = dp[i]
        return res
        