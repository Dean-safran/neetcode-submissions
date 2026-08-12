class Solution:
    def sumOfSquares(self, n) : 
            res = 0
            while n : 
                res += (n % 10) ** 2
                n //= 10
            return res
        
    def isHappy(self, n: int) -> bool:
        fast = self.sumOfSquares(self.sumOfSquares(n))
        slow = self.sumOfSquares(n)
        while True : 
            if fast == 1 or slow == 1 :
                return True
            if fast == slow :
                return False
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            slow = self.sumOfSquares(slow)
        