class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 :
            return 0
        if x == 1 :
            return 1
        if n == 0 : 
            return 1

        if n > 0 : 
            pow = n
        else :
            pow = -n

        res = 1
        while pow : 
            if (pow & 1) :
                res *= x
            x *= x
            pow >>= 1
        
        return res if n > 0 else 1/res
    
    
    # def myPow(self, x: float, n: int) -> float:
    #     #use fast exponentiation from CS334
    #     def helper(x,n) :
    #         if x == 0 :
    #             return 0
    #         if n == 0 :
    #             return 1
    #         if n == 1 :
    #             return x
    #         if n % 2 == 0 :
    #             val = helper(x,n/2)
    #             return val * val
    #         else : 
    #             return x * helper(x,n-1)
    #     if n >= 0 :
    #         return helper(x,n)
    #     else : 
    #         return 1 / helper(x,-n)

#time -> 
#o(log n) since we halve input everytime and do constant work at each 
#recursive level
#space -> 
#o(log n), each recursive call divides n by 2, so we 
#use log n call frames till we hit base case