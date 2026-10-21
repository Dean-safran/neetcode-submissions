class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {"I" : 1, "V" : 5, "X" : 10,  "L" : 50,  "C" : 100,  "D" : 500,  "M" : 1000, }

        res = 0
        prev = None
        curr = None
        ptr = len(s) - 1
        while ptr >= 0 :
            if ptr - 1 >= 0 :
                if vals[s[ptr - 1]] < vals[s[ptr]] :
                    res += vals[s[ptr]]
                    res -= vals[s[ptr - 1]]
                    ptr -= 2
                    continue
            res += vals[s[ptr]]
            ptr -= 1
        return res
            