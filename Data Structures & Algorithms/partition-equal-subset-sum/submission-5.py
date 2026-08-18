class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """

        can either include or exclude an element in the current set 



        """

        if len(nums) < 2 :
            return False 

        def sum(l) : 
            res = 0
            for i in range(len(l)) : 
                res += l[i]
            return res

        total = sum(nums)
        if total % 2 != 0 :
            return False 
        total = total // 2

        def helper(curr_sum, idx) :
            if curr_sum > total :
                return False
            if idx > len(nums) - 1 : 
                if curr_sum == total :
                    return True
                else : 
                    return False
            
            return helper(nums[idx] + curr_sum, idx + 1) or helper(curr_sum, idx + 1)

        return helper(0, 0)