class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """

        use a hashmap to store letter freq

        keep track of letters so far, 
        if letters so far freq are zero remove from 
        letters so far 
        if letters so far is empty, start a new 
        substring and append current length


        or keep track of indexes of last occurence of each letter
        """

        freq = dict()
        for ch in s : 
            if ch not in freq : 
                freq[ch] = 1
            else : 
                freq[ch] += 1

        letters_so_far = set()
        res = []
        curr_res = 0

        for i in range(0, len(s)) :
            curr_ch = s[i]
            freq[curr_ch] -= 1
            curr_res += 1
            if freq[curr_ch] == 0 :
                if curr_ch in letters_so_far : 
                    letters_so_far.remove(curr_ch)
                if not letters_so_far : 
                    res.append(curr_res)
                    curr_res = 0
            else : 
                letters_so_far.add(curr_ch)
        return res
            
            


                