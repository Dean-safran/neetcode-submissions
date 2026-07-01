class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        seen = set()
        while res != 1 :
            #reset after each pass
            res = 0
            #sum squares of digits into res
            while n != 0 :
                res += (n % 10) ** 2
                n = n // 10
            #if there is an infinite loop return false
            if res in seen :
                return False 
            #otherwise repeat summing digits with res
            #and keep track of results
            else :
                seen.add(res)
                n = res
        return True

        