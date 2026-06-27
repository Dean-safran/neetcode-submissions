class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2  :
            return max(nums)
        if len(nums) == 3 :
            return max(nums[1], nums[0] + nums[2])
        
        val0 = nums[0]
        val1 = nums[1]
        val2 = nums[0] + nums[2]
        global_max = max(val0, val1, val2)
        for i in range(3, len(nums)) :
            val3 = nums[i] + max(val0, val1)
            global_max = max(global_max, val3)
            val0 = val1
            val1 = val2
            val2 = val3
        return global_max
            






        