class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 : 
            return 0
        if n == 1 : 
            return x

        neg = n < 0 

        if neg : 
            n = abs(n)

        res = 1
        while n : 
            if n & 1 : 
                res *= x
            x *= x
            n >>= 1


        if neg : 
            return 1 / res
        else : 
            return res
        

