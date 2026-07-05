"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def end_time(self, int1) :
        return int1.end

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=self.end_time)
        for i in range(len(intervals) - 1) :
            if intervals[i+1].start < intervals[i].end :
                return False
        return True