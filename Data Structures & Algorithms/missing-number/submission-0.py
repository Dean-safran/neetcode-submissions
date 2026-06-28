class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_length = len(nums)
        total = 0
        for i in range(1, nums_length + 1) :
            total += i
        sum_of_nums = 0
        for i in range(nums_length) :
            sum_of_nums += nums[i]
        return total - sum_of_nums
