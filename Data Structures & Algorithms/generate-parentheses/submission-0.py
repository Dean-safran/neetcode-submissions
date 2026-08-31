class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """

        use two counters to keep track of parens

        the right paren stack can never be bigger than left

        use a list to accumulate curr path then join at end

        you either use one paren or the other at each step
        """

        # l is number of open parenthesis
        # r is number of closing parenthesis
        def helper(l, r) : 
            if l == 0 and r == 0 :
                res.append("".join(curr_path))
                return 
            
            if r <= l :
                curr_path.append("(")
                helper(l-1, r)
                curr_path.pop()
            else : 
                if l > 0 :
                    curr_path.append("(")
                    helper(l-1, r)
                    curr_path.pop()
                curr_path.append(")")
                helper(l, r-1)
                curr_path.pop()
            return 

        res = []
        curr_path = []
        helper(n, n)
        return res