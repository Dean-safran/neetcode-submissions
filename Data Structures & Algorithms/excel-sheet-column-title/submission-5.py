class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """

        number system base 26 instead of 2, 10 or 16

        """

        res = ""
        while columnNumber :
            columnNumber -= 1
            val = columnNumber % 26
            res = chr(val + 65) + res
            columnNumber //= 26
        return res