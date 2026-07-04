class Solution:
    def myPow(self, x: float, n: int) -> float:
        #use fast exponentiation from CS334
        def helper(x,n) :
            if x == 0 :
                return 0
            if n == 0 :
                return 1
            if n == 1 :
                return x
            if n % 2 == 0 :
                return helper(x,n/2) * helper(x,n/2)
            else : 
                return x * helper(x,n-1)
        if n >= 0 :
            return helper(x,n)
        else : 
            return 1 / helper(x,-n)