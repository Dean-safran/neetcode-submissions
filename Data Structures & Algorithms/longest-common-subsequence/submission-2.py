class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = dict()
        def helper(s1, s2) :
            if (s1, s2) in dp :
                return dp[(s1, s2)]
            curr_len = 0
            if len(s1) == 1 or len(s2) == 1 :
                if s1[0] in s2 or s2[0] in s1 : 
                    curr_len = 1
            else : 
                if s1[0] == s2[0] : 
                    curr_len = 1 + helper(s1[1:], s2[1:])
                else : 
                    curr_len = max( helper(s1[1:], s2) , helper(s1, s2[1:]) )
            dp[(s1, s2)] = curr_len
            return curr_len

        return helper(text1, text2)

         




        
