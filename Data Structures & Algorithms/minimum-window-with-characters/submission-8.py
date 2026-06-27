class Solution:
    # extend window until t requirement is met, then try and 
    # shrink the window from the left until requirment isn't met 
    # anymore, then continue to extend window from the right, 
    # keeping track of minimum sized window so far
    def minWindow(self, s: str, t: str) -> str:
        tMap = defaultdict(int)
        sMap = defaultdict(int)
        pointer1 = 0
        pointer2 = 0
        found = False
        counter = 0
        currentDiff = 10000
        result = [0,0]
        
        for ch in t :
            tMap[ch] += 1
        
        required = len(tMap)

        for pointer2 in range(len(s)):
            if s[pointer2] in tMap : 
                sMap[s[pointer2]] += 1
                if sMap[s[pointer2]] == tMap[s[pointer2]] : 
                    counter += 1
            while counter == required : 
                found = True
                if pointer2 - pointer1 < currentDiff : 
                    result[0] = pointer1
                    result[1] = pointer2
                    currentDiff = pointer2 - pointer1
                if s[pointer1] in sMap : 
                    sMap[s[pointer1]] -= 1
                    if sMap[s[pointer1]] < tMap[s[pointer1]] : 
                        counter -= 1
                pointer1 += 1
        if not found : 
            return ""
        return s[result[0] : result[1] + 1]
            




        # create a hashmap on t and s, the s hashmap
        # contains the freq of t chars in s.
        # Use sliding window on s. 

        #pointer1 = 0 pointer2 = 0, 
        
        #scan through chars of s with pointer2, 
       
        #if : counter < required (this should be 
        #the case while the outer for loop is running) : 
            #scan through s, if ch is in 
            #tMap and s, 
            #sMap[ch] += 1, if sMap[ch] == tMap[ch], counter += 1

            #everytime we add to counter check
            #to see if we have a valid substring :
            #check if counter == required (the len of tMap), if yes 
            #update shortestSubstring variable

        #while counter == required :
            #check if left pointer 
            #is in t, if yes,
            #sMap[pointer1] -= 1
            #pointer1 += 1
                # if sMap[pointer1] < tMap[pointer1], counter -= 1
            #elif left pointer is not in t, then keep incrementing
            #pointer1

        

        

        "c  abwefgew c waefgcf"

"OUZODYXAYXZ"