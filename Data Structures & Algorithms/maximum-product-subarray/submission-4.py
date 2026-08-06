class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        dp[x] is max product with subarray ending at 
        index x

        brute force is to test every subarray ending at 
        index x and return the max one
        """

        curr_min = nums[0]
        curr_max = nums[0]
        res = nums[0]
        for i in range(1, len(nums)): 
            temp_max = max(curr_min * nums[i], curr_max * nums[i], nums[i])
            curr_min = min(curr_min * nums[i], curr_max * nums[i], nums[i])
            curr_max = temp_max
            if curr_max > res : 
                res = curr_max
        return res


