class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """

        make a frequency dictionary for chars in s1

        for every potential permutation :
            make a copy of freq dict 
            increase window while char is in dict
            if char not in dict, restart window
            if dict char count reaches zero, delete from copy


        """
        def make_copy(dest, src) :
            for key in src :
                dest[key] = src[key]

        freq_dict = {}
        for ch in s1 :
            if ch in freq_dict :
                freq_dict[ch] += 1
            else :
                freq_dict[ch] = 1
        
        l = 0
        r = 0
        copy = {}
        make_copy(copy, freq_dict)

        while r < len(s2) : 
            curr_ch = s2[r]
            if curr_ch in copy :
                copy[curr_ch] -= 1
                if copy[curr_ch] == 0 :
                    del copy[curr_ch]
                if not copy :
                    return True
                r += 1
            else :
                if curr_ch in freq_dict :
                    while s2[l] != s2[r] :
                        if s2[l] not in copy :
                            copy[s2[l]] = 1
                        else :
                            copy[s2[l]] += 1
                        l += 1
                    l += 1
                    r += 1
                else :
                    make_copy(copy, freq_dict)
                    r += 1
                    l = r
        return False

        