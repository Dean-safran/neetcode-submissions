class Solution:
    def reverse(self, x: int) -> int:
        MAX = (1 << 31) - 1
        MIN = (1 << 31)
        neg = False

        if x < 0 :
            neg = True
            x = -x

        if x > MAX :
            return 0

        temp = x
        lenNum = 0
        while temp :
            temp //= 10
            lenNum += 1

        res = 0
        temp = x
        for i in range(lenNum) :
            toAdd = temp % 10
            toAdd = toAdd * (10 ** (lenNum - i - 1))
            temp //= 10
            if toAdd > MAX - res : 
                return 0
            else : 
                res += toAdd
        if neg : 
            return -res
        return res