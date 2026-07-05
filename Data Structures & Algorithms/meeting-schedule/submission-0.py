"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def compare(self, int1, int2) :
        if int1.start > int2.start :
            temp = int1
            int1 = int2
            int2 = temp
        if ((int1.end <= int2.end and int1.end > int2.start) or 
            (int1.end > int2.end) or
            (int1.start == int2.start)) :
            return False
        else :
            return True

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        val = True
        for i in range(len(intervals)) :
            for j in range(i + 1, len(intervals)) :
                val = val and self.compare(intervals[i], intervals[j])
        return val