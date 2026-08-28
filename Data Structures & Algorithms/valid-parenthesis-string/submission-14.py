class Solution:
    def checkValidString(self, s: str) -> bool:
        """

        keep track of the ->
        minimum closing parens needed
        and max closing parens needed

        a '(' inc both 
        a ')' dec both
        a '*' inc max and dec min
            -> don't set min below 0, not needed
        if max is ever less than 0, return False

        """

        l_stack = []
        s_stack = []
        freq = 0
        for i in range(len(s)) : 
            if s[i] == ')' :
                freq += 1

        for i in range(len(s)) :
            if s[i] == '(' :
                l_stack.append(i)
            elif s[i] == '*' :
                s_stack.append(i)
            else : 
                if l_stack : 
                    l_stack.pop()
                elif s_stack : 
                    s_stack.pop()
                else : 
                    return False
                freq -= 1
        while l_stack : 
            if not s_stack :
                return False
            curr_l = l_stack.pop()
            curr_s = s_stack.pop()
            if curr_l < curr_s :
                continue
            else :
                l_stack.append(curr_l)

        return True


        # min_needed = 0
        # max_needed = 0
        # for i in range(len(s)) : 
        #     if max_needed < 0 :
        #         return False
        #     if s[i] == '(' : 
        #         min_needed += 1
        #         max_needed += 1
        #     elif s[i] == ')' : 
        #         min_needed -= 1
        #         max_needed -= 1
        #     elif s[i] == '*' :
        #         min_needed = max(0, min_needed-1)
        #         max_needed += 1
        # if min_needed > 0 :
        #     return False
        # return True
       