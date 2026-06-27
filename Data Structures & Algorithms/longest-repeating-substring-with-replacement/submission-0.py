class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #  toReplace = windowLength - maxCount(the freq of the most frequent char)
        mp = defaultdict(int)
        maxCount = 0
        maxLength = 0
        l = 0
        r = 0

        for r in range(len(s)) : 
            mp[s[r]] += 1
            if mp[s[r]] > maxCount :
                maxCount = mp[s[r]]
            #if the letters needing replacement 
            #is within budget, the whole window 
            #could be the same char
            if (r - l + 1) - maxCount <= k :
                maxLength = (r - l + 1) 
            else : 
                mp[s[l]] -= 1
                l += 1
        return maxLength
            
            
            
