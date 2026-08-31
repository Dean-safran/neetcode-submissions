class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def helper(i) : 
            if i > len(nums) - 1 :
                res.append(curr_path[:])
                return 
            
            curr_path.append(nums[i])
            helper(i+1)
            curr_path.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i] :
                i += 1
            helper(i+1)

        res = []
        curr_path = []
        helper(0)
        return res