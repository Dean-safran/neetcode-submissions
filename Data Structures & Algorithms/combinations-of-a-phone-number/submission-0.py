class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """

        create dict for numbers {number:list[letters]}

        try adding a letter to curr list, if at end of 
        digits, add curr list to res
        remove letter and try next option

        """
        if not digits : 
            return []

        d = {2:['a','b','c'],
             3:['d','e','f'],
             4:['g','h','i'],
             5:['j','k','l'],
             6:['m','n','o'],
             7:['p','q','r','s'],
             8:['t','u','v'],
             9:['w','x','y','z'],
        }


        def helper(i) :
            if i > len(digits) - 1: 
                res.append("".join(curr_list))
                return
            
            for ch in d[int(digits[i])] :
                curr_list.append(ch)
                helper(i+1)
                del curr_list[-1]
        
        res = []
        curr_list = []
        helper(0)
        return res




