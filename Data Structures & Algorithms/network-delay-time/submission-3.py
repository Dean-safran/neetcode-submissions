from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = deque()
        q.append(k)

        # make node travel cost hashmap
        cost_dict = dict()
        for i in range(1, n+1) :
            cost_dict[i] = None

        cost_dict[k] = 0

        while q : 
            curr = q.popleft()
            for edge in times : 
                if edge[0] == curr :
                    next = edge[1]
                    next_val = cost_dict[next]
                    if next_val is not None :
                        cost_dict[next] = min(
                                            next_val, 
                                            cost_dict[curr] + edge[2]
                                          )
                    else : 
                        cost_dict[next] = cost_dict[curr] + edge[2]
                    if next_val is None or next_val != cost_dict[next] : 
                        q.append(next)

        max = -1
        for node in cost_dict : 
            if cost_dict[node] is None : 
                return -1
            if cost_dict[node] > max :
                max = cost_dict[node]
        return max
            

                    