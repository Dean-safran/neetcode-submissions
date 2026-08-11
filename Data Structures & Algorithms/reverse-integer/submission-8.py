class Solution:
    def reverse(self, x: int) -> int:
        MAX = (1 << 31) - 1
        MIN = -(1 << 31)
        neg = x < 0
        res = 0
        while x : 
            if neg : 
                temp = -x
                toAdd = temp % 10
                toAdd = -toAdd
            else : 
                toAdd = x % 10
                
            if (MAX // 10) < res or (MAX // 10) == res and toAdd > MAX % 10 :
                return 0
            elif (MIN // 10) > res or (MIN // 10) == res and toAdd < MIN % 10 :
                return 0
            else : 
                res *= 10
                res += toAdd
                x = int(x / 10)
        return res

