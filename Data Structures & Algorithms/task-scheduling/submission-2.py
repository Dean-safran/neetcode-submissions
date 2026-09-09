import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        make freq map

        
        """
        freq = dict()
        freq_heap = []
        cool_down = deque()
        res = 0
        for task in tasks : 
            if task not in freq :
                freq[task] = 1
            else : 
                freq[task] += 1

        for task in freq : 
            heapq.heappush(freq_heap,(-freq[task], task))
        
        time = 0
        while freq_heap or cool_down: 
            if freq_heap : 
                time += 1
                curr_freq, curr_task = heapq.heappop(freq_heap)
                curr_freq = (-curr_freq) - 1
                if curr_freq > 0 :
                    cool_down.append((time + n, curr_freq, curr_task))
            else : 
                # use cooled down task and 
                # fast forward time 
                curr_time, curr_freq, curr_task = cool_down.popleft()
                time = curr_time
                time += 1
                curr_freq -= 1
                if curr_freq > 0 :
                    cool_down.append((time+n, curr_freq, curr_task))
            while cool_down and cool_down[0][0] == time :
                curr_time, curr_freq, curr_task = cool_down.popleft()
                heapq.heappush(freq_heap, (-curr_freq, curr_task))
        return time



                
                
                
                    