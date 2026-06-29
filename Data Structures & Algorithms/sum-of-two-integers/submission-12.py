class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = False
        for i in range(0,32) :
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            if (bit_a == 0) and (bit_b == 0) :
                if carry :
                    carry = False
                    res += 1 << i
                else :
                    continue
            elif (bit_a == 1) and (bit_b == 1) :
                if carry :
                    res += 1 << i
                else :
                    carry = True
            else :
                if carry :
                    continue
                res += 1 << i
        if res > 0x7fffffff :
            res = res ^ ((2 ** 32) - 1)
            res = ~res
        return res 