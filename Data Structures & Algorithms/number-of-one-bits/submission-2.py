class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32) :
            ans += n % 2
            n = n // 2
        return ans