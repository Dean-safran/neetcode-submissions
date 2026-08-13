class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """

        Either add or subtract the current number 
        recursive approach :
            num ways at curr_num with target_amount left
            is f(next_num, target + curr_num) +
               f(next_num, target - curr_num)

            if target_amount == 0 : return 1
            if target_amount < 0 or next_num out of range: return 0

        """

       
        sum = 0  # sum is also offset for memo table
        for i in range(len(nums)) : 
            sum += abs(nums[i])
        total_len = (2 * sum) + 1
        if abs(target) > sum : 
            return 0
        dp = [[0 for _ in range(total_len)] for _ in range(len(nums) + 1)]

        # base case -> there is one way to 
        # make target 0 with no coins : use no coins
        dp[len(nums)][sum] = 1

        # fill in dp table
        for i in range(len(nums) - 1, -1, -1) : 
            for t in range(total_len) :
                val = 0
                if t - nums[i] >= 0 :
                    val += dp[i+1][t - nums[i]]
                if t + nums[i] <= total_len - 1 :
                    val += dp[i+1][t + nums[i]]
                dp[i][t] = val

        return dp[0][target + sum]
        


        # dp = dict()
        # def helper(idx, target_amount) :
        #     if (idx, target_amount) in dp :
        #         return dp[(idx, target_amount)]

        #     if target_amount == 0 and idx == len(nums):
        #         return 1
        #     if idx > len(nums) - 1 :
        #         return 0

        #     num_ways = 0
        #     num_ways += helper(idx + 1, target_amount + nums[idx])
        #     num_ways += helper(idx + 1, target_amount - nums[idx])

        #     dp[(idx, target_amount)] = num_ways
        #     return num_ways
        
        # return helper(0, target)



