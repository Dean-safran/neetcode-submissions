class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        best_starting_idx = -1
        possible_starting_idx = -1
        curr_streak = 0
        max_streak = -1
        running_sum = 0

        for i in range(len(gas)) :
            curr_val = gas[i] - cost[i]
            running_sum += curr_val

            if curr_val >= 0 and curr_streak == 0:
                possible_starting_idx = i
            if curr_val >= 0 :
                curr_streak += curr_val
                if curr_streak > max_streak :
                    best_starting_idx = possible_starting_idx
            elif curr_val < 0 : 
                curr_streak = 0
            
        if running_sum < 0 :
            return -1
        else :
            return best_starting_idx