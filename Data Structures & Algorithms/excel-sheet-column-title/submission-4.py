class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """

        number system base 26 instead of 2, 10 or 16

        """

        res = ""
        while columnNumber :
            val = columnNumber % 26
            if val == 0 :
                val = 26
            res = chr(val + 64) + res
            if columnNumber == 26 :
                return res
            columnNumber //= 26
        return res