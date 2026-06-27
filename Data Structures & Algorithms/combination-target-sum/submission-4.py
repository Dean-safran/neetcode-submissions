class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        start = 0
        
        def backtrack(start, added_so_far):
            nonlocal result
            count = 0
            if len(added_so_far) == 10 : 
                start += 1
                return 
            else : 
                for i in range(len(added_so_far)) : 
                    count += added_so_far[i]
                if count == target : 
                    result += [added_so_far[:]]


                for i in range(start, len(nums)) : 
                    added_so_far.append(nums[i])
                    backtrack(i, added_so_far)
                    added_so_far.pop()
        backtrack(start, [])
        return result

            