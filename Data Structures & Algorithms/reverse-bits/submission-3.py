class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32) :
            curr_bit = (n >> i) & 1
            curr_bit = curr_bit << (31-i)
            res += curr_bit  
        return res
        

