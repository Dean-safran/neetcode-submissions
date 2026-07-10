class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])

        res = []
        to_add = intervals[0]
        for i in range(len(intervals) - 1) :
            if to_add[1] < intervals[i + 1][0] : 
                res.append(to_add)
                to_add = intervals[i+1]
            else :
                to_add[1] = max(to_add[1], intervals[i+1][1])
        res.append(to_add)
        return res