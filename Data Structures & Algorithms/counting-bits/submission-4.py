class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1) :
            curr = i
            num_ones = 0
            for _ in range(32) :
                num_ones += curr % 2
                curr = curr // 2
            ans += [num_ones]
        return ans