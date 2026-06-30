class Solution:
    def reverse(self, x: int) -> int:
        MAX = (2 ** 31) - 1
        MIN = -(2 ** 31)
        neg = False
        if x < 0 :
            x = -x
            neg = True
        #determine number of digits in x
        num_digits = 0
        temp = x
        while temp != 0 :
            num_digits += 1
            temp = temp // 10
        res = 0
        for i in range(num_digits) :
            #isolate digit
            digit = (x // (10 ** i)) % 10
            #move digit to reversed spot
            digit = digit * (10 ** ((num_digits - 1) - i))
          #add to total
            res += digit
        if res > MAX or res < MIN : 
            return 0
        if neg :
            res = -res
        return res
            
#time o(n), n being the amount of numbers 
#in x. We loop though each digit in x and 
#use constant time ops to move them to reversed
#spot
#space o(1), for flags and variables
