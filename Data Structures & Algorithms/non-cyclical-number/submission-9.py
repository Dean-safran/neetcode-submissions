class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True :
            res = 0
            while n :
                res += (n % 10) ** 2
                n //= 10
            if res == 1 :
                return True
            else : 
                if res in seen :
                    return False
                seen.add(res)
                n = res


        