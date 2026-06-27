class Solution:
    def isValid(self, s: str) -> bool:
        #for ch in s, add to stack. 

        # intialize two hashmaps called 'open' 
        # and 'closed', each bracket
        # pair in each map will have the same value, 
        # 1,2 or 3

        # if current ch is in closed, peek onto 
        # stack to see what prev element is, if 
        # open[stack[-1]] != closed[ch], return false

        # if they are equal, pop the pair of chars off the 
        # stack :)

        stack = []
        openBrackets = { "(" : 1, "[" : 2, "{" : 3 }
        closedBrackets =  { ")" : 1, "]" : 2, "}" : 3 }

        for ch in s : 
            if ch in closedBrackets : 
                if len(stack) == 0 : 
                    return False
                if openBrackets[stack[-1]] != closedBrackets[ch] : 
                    return False
                stack.pop()
            else :
                stack.append(ch)
        if len(stack) == 0 :
            return True 
        return False




