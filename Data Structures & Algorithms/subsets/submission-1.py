class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        there are 2^n final subsets, each time we 
        reach a final subset, we copy before modifying 
        the list and backtracking, therefore the time 
        complexity is O(n* 2^n).

        space complexity is O(2^n) for output list
        and O(n) space for recursion stack. 

        """
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