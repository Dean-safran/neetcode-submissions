class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [nums[0]]
        for i in range(len(nums) - 1) :
            # if next num is greater than sum so far
            if nums[i + 1] > sums[i] :
                # extend if sum so far is positive
                if sums[i] > 0 :
                    sums.append(sums[i] + nums[i+1])
                # stop accumulating if sum so far doesn't contribute
                else : 
                    sums.append(nums[i+1])
            # otherwise extend sum so far
            else : 
                sums.append(sums[i] + nums[i+1])
        return max(sums)
