# since you can't use adjacent houses, my thought was to find
# the total of all the even indexed houses, then odd indexed houses 
# and take the maximum. But what if the best option has houses 
# that are even indexed AND houses that are odd indexed?

# e.g. : [1, 99, 1, 1, 99], the best option here is clearly to 
# rob both houses with 99, so the max(even, odd) approach wouldn't 
# work. 

# Therefore when evaluating best value robbing ending at house i, 
# you must look at the best value robbing 
# ending at house i-2 and i-3, and sum i + max(i-2, i-3). This ensures 
# we look at all scenarios of combinations of even or odd indexed houses

"""
time o(n) to scan nums array, space o(1) for pointers
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2  :
            return max(nums)
        
        val0 = nums[0]
        val1 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)) :
            val2 = max(val0 + nums[i], val1)
            val0 = val1
            val1 = val2
            
        return val2
            






        