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

        # Again, had to look up prefix suffix multiplication : a dp-esque approach
        # where prefix[i] is the product of every num before nums[i] 
        # and suffix[i] is the product of every num after nums[i]. We use 
        # prefix[i-1] to calculate prefix[i], and suffix[i+1] to calculate suffix[i].
        # This is a constant two number multiplication operation to form 
        # each element in the memoization structures and then a constant 
        # multiplication operation for all numbers before and after nums[i], using 
        # prefix[i] and suffix[i], to form each element in the output array.

        # Three o(n) operations total o(n) time and space.
        

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

        