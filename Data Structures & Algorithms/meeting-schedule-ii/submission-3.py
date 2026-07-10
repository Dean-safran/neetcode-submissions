"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # create room_counter
        # create overlap list

        # while keep_removing_overlap : 

            # sort intervals by ending times

            # place least amount of overlapping
            # intervals into an overlapping list

            # if overlapping list is empty, keep_removing overlap = false
            # if not empty, add to counter, set intervals to overlapping list, 
            # reset overlap list, repeat

        if not intervals : 
            return 0

        room_counter = 1
        overlap_list = []
        keep_removing_overlap = True
        intervals.sort(key=lambda x : x.start)

        while keep_removing_overlap : 
            r = intervals[0].end
            for i in range(len(intervals) - 1): 
                if r <= intervals[i + 1].start : 
                    r = intervals[i + 1].end
                else : 
                    overlap_list.append(intervals[i + 1])
            #if overlap list is empty, stop removing overlap
            if not overlap_list : 
                keep_removing_overlap = False
            else : 
                room_counter += 1
                intervals = overlap_list
                overlap_list = []
        return room_counter
        