class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """

        Need two functions, an addition 
        helper, a multiplication, helper 
        with a trailing zeroes param


        """

        def add(num1 : str, num2 : str) :
            if num1 == "0" :
                return num2
            if num2 == "0" :
                return num1
            num1 = num1[::-1]
            num2 = num2[::-1] 
            if len(num1) < len(num2) :
                temp = num1
                num1 = num2
                num2 = temp
            res = ""
            carry = 0
            for i in range(0, len(num1)) : 
                if i < len(num2) :
                    curr = int(num1[i]) + int(num2[i])
                    curr += carry
                    carry = curr // 10
                    str_curr = str(curr)
                    res += str_curr[-1]
                else : 
                    curr = int(num1[i])
                    curr += carry
                    carry = curr // 10
                    str_curr = str(curr)
                    res += str_curr[-1]
            if carry > 0 : 
                res += str(carry)
            return res[::-1]

        def mult(num, dig, zeroes) : 
            zeroes_to_add = "0" * zeroes
            if dig == "0" :
                return "0"
            if dig == "1" :
                return num + zeroes_to_add
            num = num[::-1]
            dig = int(dig)
            res = ""
            carry = 0
            for i in range(len(num1)) : 
                curr = int(num[i]) * dig
                curr += carry
                carry = curr // 10
                str_curr = str(curr)
                res += str_curr[-1]
            if carry > 0 :
                res += str(carry)
            return res[::-1] + zeroes_to_add
        

        to_add = []
        if len(num1) < len(num2) :
            temp = num1
            num1 = num2
            num2 = temp
        for i in range(len(num2) - 1, -1, -1) :
            to_add.append(mult(num1, num2[i], len(num2) - 1 - i))
        res = "0"
        for i in range(0, len(to_add)) : 
            res = add(res, to_add[i])
        return res
                

                    