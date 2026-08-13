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
        dp = dict()
        def helper(idx, target_amount) :
            if (idx, target_amount) in dp :
                return dp[(idx, target_amount)]

            if target_amount == 0 and idx == len(nums):
                return 1
            if idx > len(nums) - 1 :
                return 0

            num_ways = 0
            num_ways += helper(idx + 1, target_amount + nums[idx])
            num_ways += helper(idx + 1, target_amount - nums[idx])

            dp[(idx, target_amount)] = num_ways
            return num_ways
        
        return helper(0, target)