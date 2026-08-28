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


        min_needed = 0
        max_needed = 0
        for i in range(len(s)) : 
            if max_needed < 0 :
                return False
            if s[i] == '(' : 
                min_needed += 1
                max_needed += 1
            elif s[i] == ')' : 
                min_needed -= 1
                max_needed -= 1
            elif s[i] == '*' :
                min_needed = max(0, min_needed-1)
                max_needed += 1
        if min_needed > 0 :
            return False
        return True
       