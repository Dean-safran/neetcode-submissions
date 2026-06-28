class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Subtract the numbers in the list
        # from the sum of n -> 0
        # The result is the missing num
        res = len(nums)
        for i in range(len(nums)) :
            res += (i - nums[i])
        return res

#time -> o(n)
#space -> o(1)
