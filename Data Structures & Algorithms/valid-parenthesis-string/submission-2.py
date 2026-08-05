class Solution:
    def checkValidString(self, s: str) -> bool:
        l_stack = []
        s_stack = []

        for i, c in enumerate(s) : 
            if c == "(" :
                l_stack.append(i)
            elif c == "*" :
                s_stack.append(i)
            elif c == ")" :
                if l_stack : 
                    l_stack.pop()
                elif s_stack : 
                    s_stack.pop()
                else : 
                    return False
        while l_stack and s_stack: 
            if l_stack[-1] > s_stack[-1] :
                return False
            else : 
                l_stack.pop()
                s_stack.pop()
        if l_stack :
            return False
        return True


        

        

