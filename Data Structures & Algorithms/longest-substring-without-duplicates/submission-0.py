class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create two pointers, and a hash table of where 
        # elements were, if we encounter a duplicate, 
        # keep track of length and set pointer1 equal 
        # to the place the duplicate was last, decrement 
        # counter by pointer1 new - pointer1 old and 
        # loop through the elements up to where the 
        # pointer1 was originally, then delete them 
        # from hash table. 
        # This only happens once per element max so its o(n).

        #overall running time would be o(n)

        pointer1 = 0
        tb = {}
        counter = 0
        maxCount = 0
        for pointer2 in range(len(s)) : 
            counter += 1
            if s[pointer2] not in tb : 
                tb[s[pointer2]] = pointer2
                maxCount = max(maxCount, counter)
            else : 
                lastSeen = tb[s[pointer2]]
                pointer1Temp = pointer1
                pointer1 = lastSeen + 1
                counter -= pointer1 - pointer1Temp
                for i in range(pointer1Temp, lastSeen) :
                    del tb[s[i]]
                tb[s[pointer2]] = pointer2
        return maxCount      





