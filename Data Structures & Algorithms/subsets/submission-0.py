class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(curr_list, i) :
            if i > len(nums) - 1 :
                res.append(curr_list)
                return 
            
            new_list = curr_list + [nums[i]]
            helper(new_list, i + 1)
            list2 = new_list.copy()
            list2.pop()
            helper(list2, i + 1)
        
        helper(res, 0)
        return res