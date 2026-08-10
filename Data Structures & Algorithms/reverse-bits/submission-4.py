class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32) :
            temp = n
            temp >>= i
            temp &= 0x1
            temp <<= (31 - i)
            res += temp
        return res

        

