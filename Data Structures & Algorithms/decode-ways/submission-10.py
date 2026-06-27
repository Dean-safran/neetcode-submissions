class Solution:
    def numDecodings(self, s: str) -> int:
        
        pointer_nextnext = -1
        pointer_next = -1
        pointer_new = -1
        for i in range(len(s) - 1, -1, -1) :
            #base cases 
            if i == len(s) - 1:
                if s[i] == "0":
                    pointer_nextnext = 0
                else :
                    pointer_nextnext = 1
            elif i == len(s) - 2 :
                if s[i] == "0" :
                    pointer_next = 0
                elif ( (int(s[i] + s[i+1]) > 26) or
                       s[i+1] == "0" ) :
                    pointer_next = 1
                else :
                    pointer_next = 2
            #base cases
            else :
                pointer_new = 0 #reset new number
                if s[i] == "0" :
                    pointer_nextnext = pointer_next
                    pointer_next = pointer_new
                    continue
                if pointer_next != 0:
                    pointer_new += pointer_next
                if ( int(s[i] + s[i+1]) < 27 and pointer_nextnext != 0 ) :
                    pointer_new += pointer_nextnext
                pointer_nextnext = pointer_next
                pointer_next = pointer_new

        #handles strings of (len < 3) when pointers may not be filled yet
        if pointer_next == -1 :
            return pointer_nextnext
        if pointer_new == -1 :
            return pointer_next
        return pointer_new