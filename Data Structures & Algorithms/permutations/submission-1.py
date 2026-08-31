class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """

        of the spots, for each element in nums try using it in that spot, 
        then backtrack and pick next element and move on without that element

        curr_path is o(n) space, time complexity is o(n! * n) because 
        we copy the path into result for every permutation and copy current options
        as we recurse to preserve loop order. (don't want to loop 1,2,3, use 1, then 
        append 1 when we're done and loop over 2,3,1, we'd repeat 1)
        """

        def helper(curr_options) :
            if not curr_options : 
                res.append(curr_path[:])
                return 

            curr_options_copy = curr_options.copy()
            for option in curr_options :
                curr_path.append(option)
                curr_options_copy.remove(option)
                helper(curr_options_copy)
                curr_path.remove(option)
                curr_options_copy.append(option)
        
        res = []
        curr_path = []
        helper(nums)
        return res
