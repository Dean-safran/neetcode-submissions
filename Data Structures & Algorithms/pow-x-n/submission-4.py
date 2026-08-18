class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n) : 
            if n == 0 : 
                return 1
            if n == 1 : 
                return x
            if n % 2 != 0 :
                return x * helper(x, n-1)
            else : 
                val = helper(x, n // 2)
                return val * val
        neg = n < 0
        if neg : 
            res = helper(x, -n)
            return 1 / res
        else : 
            res = helper(x, n)
            return res
        

