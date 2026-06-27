class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       #Intuition
        # you only want to delete the relevant 
        # portion of the window that violates 
        # the consecutive uniqueness property, 
        # which requires deletion of everything 
        # before and including the previously 
        # seen duplicate

       #Method 
        # create two pointers, and a hash table of where 
        # elements were, if we encounter a duplicate, 
        # keep track of length and set pointer1 equal 
        # to the place the duplicate was last, decrement 
        # counter by pointer1 new - pointer1 old and 
        # loop through the elements up to where the 
        # pointer1 was originally, then delete them 
        # from hash table. 
        # This only happens once per element max so its o(n).

       #Time and Space
        #overall running time would be o(n) with o(n) space 
        # for hashtable. Every char in s only gets
        # added and removed once, so total is o(n)
        # space, including the loop in the else block


        # pointer1 = 0
        # tb = {}
        # counter = 0
        # maxCount = 0
        # for pointer2 in range(len(s)) : 
        #     counter += 1
        #     if s[pointer2] not in tb : 
        #         tb[s[pointer2]] = pointer2
        #         maxCount = max(maxCount, counter)
        #     else : 
        #         lastSeen = tb[s[pointer2]]
        #         pointer1Temp = pointer1
        #         pointer1 = lastSeen + 1
        #         counter -= pointer1 - pointer1Temp
        #         for i in range(pointer1Temp, lastSeen) :
        #             del tb[s[i]]
        #         tb[s[pointer2]] = pointer2
        # return maxCount     

        mp = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in mp:
                #if previously seen element is farther 
                #back than the current l pointer because 
                #we already encountered a duplicate, 
                #keep l where it's at
                l = max(mp[s[r]] + 1, l) 
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res 





