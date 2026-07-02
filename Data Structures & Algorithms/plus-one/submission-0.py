class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        #determine length of array 
        length = len(digits)
        #loop from end of array to beginning
        #inclusive of 0
        for i in range(length - 1, -1, -1) :
            #regular increment case
            if digits[i] < 9 :
                digits[i] += 1 
                return digits
            #carry over case
            elif digits[i] == 9 and i > 0 :
                digits[i] = 0
            #carry over and add a new order case
            elif digits[i] == 9 and i == 0 :
                digits[i] = 0
                new_digits = [1]
                for i in range(len(digits)) :
                    new_digits.append(digits[i])
                digits = new_digits
        return digits
        
            