""" o(t/m) space where t is the target and m is the smallest 
element in the array

We either add an number or we don't and move on, the max height 
of the tree would be choosing the smallest element in the array 
over and over, the smallest element (m) would fit into target 
t/m times. See goodnotes for recursion tree big o analysis

"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start, added_so_far, total):
            nonlocal result
            if total == target : 
                result.append(added_so_far[:])
                return 

            for i in range(start, len(nums)) : 
                if total + nums[i] > target : 
                    return
                added_so_far.append(nums[i])
                backtrack(i, added_so_far, total + nums[i])
                added_so_far.pop()
        backtrack(0, [], 0)
        return result

            