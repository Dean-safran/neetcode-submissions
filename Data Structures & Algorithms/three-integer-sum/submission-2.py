class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        # fixed number gets set, scan rest of array w two
        # pointers. If nums[pointer1] + nums[pointer2]
        # < target, increment pointer1 by 1, if >
        # target, decrement pointer2 by 1. if sum equals 
        # target, increment both until both numbers 
        # are different

        [-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]
        nums = sorted(nums)
        result = []
        for i in range(len(nums) - 2) : 
            if i > 0 and nums[i] == nums[i-1] : 
                continue
            prevPoint1 = None
            prevPoint2 = None
            pointer1 = i + 1
            pointer2 = len(nums) - 1
            target = -(nums[i])

            while pointer1 < pointer2 :
                if nums[pointer1] == prevPoint1 :
                    pointer1 += 1
                    continue
                if nums[pointer2] == prevPoint2 : 
                    pointer2 -= 1
                    continue 
                if nums[pointer1] + nums[pointer2] == target:
                    prevPoint1 = nums[pointer1]
                    prevPoint2 = nums[pointer2]
                    toAdd = [nums[i], nums[pointer1], nums[pointer2]]
                    result += [toAdd]
                    pointer1 += 1
                    pointer2 -= 1
                elif nums[pointer1] + nums[pointer2] < target:
                    pointer1 += 1
                elif nums[pointer1] + nums[pointer2] > target:
                    pointer2 -= 1
        return result   




        
        


# slower versions I came up with : 

        # sort nums
        # create hash table with numbers and their indexes

        # pointer1 goes up to n-2, pointer2
        # goes up to n-1, for each pair, check if 
        # target, which is 
        # 0 - (nums[pointer1] + nums[pointer2]) 
        # exists in hashtable, check if tb[target] > pointer2

        #  if yes add list to result
        

        #creating all unique triplet sets that have unique 
        #elements is o(n! / k!(n-k)!), I found an algorithm that 
        #creates these sets intrinsically! So my running time is 
        # o(that equation) x o(k), because you need to add k elements 
        # to each list that gets checked for sum == 0, 
        # but k is small (3 here) so we ignore

        # time complexity is therefore o(n choose 3)
        # [n x (n-1) x (n-2) / 3 x 2 x 1 ] is o(n^3)

        # algorithm : iterate 3 pointers over all numbers 
        # making sure pointer1 < pointer2 < pointer3, 
        # pointer 1 will iterate over all n numbers, 
        # pointer 2 will iterate over n-1 numbers, 
        # pointer 3 n-2 
        






        # combinatorics explained : 

        # you have 5 options for the first index, 
        # 4 options for the second (as to not repeat the 
        # first element) and 3 options for the third, same 
        # reasoning. That's 5 x 4 x 3 options. This, however,
        # has repeated permutations per set with uniquue 
        # elements. More specifically, each set at 3!
        # permutations -- the amount of ways to rearrange 
        # 3 numbers in the triplet. So you divide out 
        # 3! because you only want one unique version 
        # of each set. So the overall amount is 
        # n! / k! (n-k)! , you divde out the (n-k)!
        # because in 5 x 4 x 3 x 2 x 1 (like our example)
        # you only want 5 x 4 x 3. So you divide out 
        # 2 x 1, and you divide out 3! to get unique sets 
        # (each unique triplet set has 3! versions)




