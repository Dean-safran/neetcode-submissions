class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """

        at each char there are a few cases 

        add char to substring of s1 (if possible)

        add char to substring of s2 (if possible)

        start new substring for s1 

        start new substring for s2

        for each case, we need to keep track of the curr
        index for s1 and s2

        """
        if s1 == "" :
            return s2 == s3
        if s2 == "" :
            return s1 == s3
        if s1 == s2 and s1 == "" :
            return s1 == s3
        if len(s1) + len(s2) != len(s3) : 
            return False
 
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(1, len(s2) + 1) : 
            dp[0][i] = (s3[i-1] == s2[i-1]) and dp[0][i - 1] 
        
        for i in range(1, len(s1) + 1) : 
            dp[i][0] = (s3[i-1] == s1[i-1]) and dp[i - 1][0]

        for i in range(1, len(s1) + 1) :
            for j in range(1, len(s2) + 1) :
                # adding a letter from s1 is valid 
                if dp[i-1][j] :
                    if s1[i-1] == s3[i + j - 1] :
                        dp[i][j] = True
                # adding a letter from s2 is valid
                if dp[i][j-1] :
                    if s2[j-1] == s3[i + j - 1] :
                        dp[i][j] = True
                
        return dp[len(s1)][len(s2)] 


        
