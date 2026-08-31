class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def DFS(i, left) : 
            if left == 0 : 
                res.append(curr_path[:])
                return
            
            if left < 0 or i > len(candidates) - 1:
                return
            
            curr_path.append(candidates[i])
            new_left = left - candidates[i]
            DFS(i+1, new_left)
            curr_path.pop()
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i] :
                i += 1
            DFS(i+1, left)

        candidates.sort()
        res = []
        curr_path = []
        DFS(0, target)
        return res