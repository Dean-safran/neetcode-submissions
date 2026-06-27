class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 1 :
            return [[strs[0]]]
        if len(strs) == 1 and strs[0] == "" :
            return [strs[0]]


        d = {}
        for s in strs:
            sig = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for ch in s : 
                ch_num = ord(ch) - 97
                sig[ch_num] += 1
            sig = tuple(sig)
            if sig not in d :
                d[sig] = [s]
            else : 
                d[sig] += [s]

        result = []
        for key in d:
            result += [d[key]]
        return result


        

                 
             