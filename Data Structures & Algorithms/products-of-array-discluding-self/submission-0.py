class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create a hashmap of numbers and their indexes
        # , if 0 is in the hashmap everything 
        # except the index where 0 is is 0, scanning and multiplying 
        # the rest of the array should be o(n) 
        # if 0 has two indexes, return all 
        # zeroes

        # a naive o(n) approach for the non zero case could be calculating 
        # the total product, then each ouput[i] would be (total / nums[i])

        # But since we can't divide, we'd have to compute the product of every
        # num before and after nums[i], that's multiplying n-1 numbers n times
        # which is o(n^2)

        prefix = [1] * len(nums)
        for i in range(len(nums)) :
            if i == 0 :
                prefix[i] = 1
            else :
                prefix[i] = prefix[i-1] * nums[i-1]

        suffix = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1) :
            if i == len(nums) - 1 :
                suffix[i] = 1
            else : 
                suffix[i] = suffix[i+1] * nums[i+1]
        
        output = [1] * len(nums) 
        for i in range(len(nums)) : 
            output[i] = prefix[i] * suffix[i] 
        return output

        