class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # returns first index greater than num
        # if it exists
        def binSearch(l, r, nums, num) :
            if len(nums) < 1 : 
                return -1

            if l > r :
                return l

            m = (l + r) // 2

            if num > nums[m] :
                return binSearch(m+1, r, nums, num)
            elif num <= nums[m] :
                return binSearch(l, m-1, nums, num)

        dp = []

        for i in range(0, len(nums)) : 
            if len(dp) == 0 or nums[i] > dp[-1] : 
                dp.append(nums[i])
            else :
                # there is a larger number than 
                # curr in dp that can be replaced
                idx = binSearch(0, len(dp) - 1, dp, nums[i])
                if idx == -1 :
                    continue
                dp[idx] = nums[i]
        return len(dp)

            



        