class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # bin search left 
        def binSearch(l, r, intervals, start) : 
            if l > r : 
                return r
            
            m = (l + r) // 2

            if intervals[m][0] < start : 
                return binSearch(m+1, r, intervals, start)
            elif intervals[m][0] > start :
                return binSearch(l, m-1, intervals, start)
            else : 
                return m
        
        prev = binSearch(0, len(intervals)-1, intervals, newInterval[0])

        next = prev + 2

        intervals.insert(prev + 1, newInterval)

        # merge left?
        while prev > -1 and intervals[prev][1] >= newInterval[0] :
            intervals[prev + 1][0] = min(newInterval[0], intervals[prev][0])
            intervals[prev + 1][1] = max(newInterval[1], intervals[prev][1])
            del intervals[prev]
            prev -= 1
            next -= 1

        # merge right?
        while next < len(intervals) and intervals[next][0] <= newInterval[1] :
            intervals[prev + 1][0] = min(newInterval[0], intervals[next][0])
            intervals[prev + 1][1] = max(newInterval[1], intervals[next][1])
            del intervals[next]

            

        return intervals
            