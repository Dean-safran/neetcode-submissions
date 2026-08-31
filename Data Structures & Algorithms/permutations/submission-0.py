class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """

        of the spots, for each element in nums try using it in that spot, 
        then backtrack and pick next element and move on without that element

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
