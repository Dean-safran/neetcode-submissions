class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = False
        for i in range(32) :
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            sum_bit = 0
            if bit_a and bit_b :
                if carry :
                    sum_bit = 1
                else :
                    sum_bit = 0
                    carry = True
            elif bit_a or bit_b :
                if carry : 
                    sum_bit = 0
                else : 
                    sum_bit = 1
            elif not bit_a and not bit_b :
                if carry :
                    sum_bit = 1
                else :
                    sum_bit = 0
                carry = False
            sum_bit <<= i
            res += sum_bit
        if sum_bit : 
            neg = -1 << 32
            return neg | res
        return res
