class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # each letter appears at most once in a substring

        last_occurences = dict()

        for i in range(len(s)) : 
            curr_letter = s[i]
            last_occurences[curr_letter] = i

        curr_partition_start = -1
        curr_partition_end = -1
        curr_end_letter = None
        res = []
        for i in range(len(s)) :
            curr_letter = s[i] 
            if i > curr_partition_end :
                curr_partition_start = i
                curr_partition_end = last_occurences[curr_letter]
                curr_end_letter = curr_letter
                res.append(curr_partition_end - curr_partition_start + 1)
                if curr_partition_end == len(s) - 1 :
                    break
            else : 
                if curr_letter == curr_end_letter : 
                    continue
                elif last_occurences[curr_letter] > curr_partition_end : 
                    curr_partition_end = last_occurences[curr_letter]
                    res[-1] = curr_partition_end - curr_partition_start + 1
                    curr_end_letter = curr_letter
        return res

                