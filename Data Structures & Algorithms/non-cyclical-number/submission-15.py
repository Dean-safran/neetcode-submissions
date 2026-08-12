class Solution:
    """
    time for happy number is log(n), because 
    any number n has log_10(n) digits, and we process 
    those digits. After, the cycle detection works on 
    very small numbers (81 * number of digits, since 9
    is the biggest digit to be processed) which is constant 
    extra time. 
    """
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
        