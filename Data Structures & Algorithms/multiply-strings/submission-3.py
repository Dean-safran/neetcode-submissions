class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0" :
            return "0"
        
        dict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        dict2 = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}


        int1 = 0
        len1 = len(num1) - 1
        for i in range(len(num1) - 1, -1, -1) :
            int1 += (10 ** (len1 - i)) * dict[num1[i]]
        
        int2 = 0
        len2 = len(num2) - 1
        for i in range(len(num2) - 1, -1, -1) :
            int2 += (10 ** (len2 - i)) * dict[num2[i]]
        
        int_res = int1 * int2
        res = ""
        while int_res != 0 :
            res = dict2[int_res % 10] + res
            int_res //= 10
        
        return res