

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2 :
            return max(nums)
        
        def dp_pass(starting_at, ending_at) :
            if (ending_at - starting_at) == 1 :
                return max(nums[starting_at: ending_at + 1])
            
            val1 = nums[starting_at]
            val2 = max(nums[starting_at], nums[starting_at + 1])

            for i in range(starting_at + 2, ending_at + 1) :
                val3 = max(val1 + nums[i], val2)
                val1 = val2
                val2 = val3
            return val3
        one = dp_pass(0, len(nums) - 2)
        two = dp_pass(1, len(nums) - 1)
        return max(one, two)
