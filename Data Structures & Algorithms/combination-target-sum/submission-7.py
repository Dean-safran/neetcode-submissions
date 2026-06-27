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
                total += nums[i]
                if total > target : 
                    return
                added_so_far.append(nums[i])
                backtrack(i, added_so_far, total)
                added_so_far.pop()
                total -= nums[i]
        backtrack(0, [], 0)
        return result

            