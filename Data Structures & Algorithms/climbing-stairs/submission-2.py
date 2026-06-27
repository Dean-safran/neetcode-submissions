#o(n) time o(1) space

class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(2, n + 1) :
            temp = two
            new = one + two
            one = temp
            two = new
        return two
