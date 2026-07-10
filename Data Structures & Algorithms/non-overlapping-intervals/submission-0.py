class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        l = intervals[0][0]
        r = intervals[0][1]
        res = 0
        for i in range(len(intervals) - 1) :
            if r <= intervals[i + 1][0] : 
                l = intervals[i + 1][0]
                r = intervals[i + 1][1]
            else : 
                res += 1
        return res