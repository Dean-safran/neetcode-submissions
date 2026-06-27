class Solution:
    def findMin(self, nums: List[int]) -> int:

        # moving pointers essentially removes half the array each
        # time, working with the final 2 numbers 
        # where the break in the ascending order might be
        # is constant time because it's only three elements
        # overall o(log n) time with o(1) space in the context 
        # of the new list for final portion always being 
        # a constant, very small 2 elements logn

        l = 0
        r = len(nums) - 1

        if len(nums) == 1 : 
            return nums[0]

        while r - l > 1 : 
            mid = l + ( (r - l) // 2 )
            if nums[l] > nums[mid] : 
                r = mid
            else : 
                l = mid
        
        finalPortion = nums[l : r + 1]
        if nums[l] < nums[l+1] :
            return nums[0]
        return min(finalPortion)
            
            

 #I want to find the break where the end meets the beg
        # of the array if the array is shifted

        # the left side is what's always out of order

        # start in the middle, if the out-of-orderness is 
        # not to the left of this number, it could be to the right
        # so recurse to the right, start in the middle and get rid of half 
        # the array

        # start left pointer at 0, right at end, and mid at 
        # (right - left) // 2 

        # if mid < left, recurse on left, otherwise recurse on 
        # right

        # if you find an element where the number to the left
        # is larger you found min, base case is < 2 elements, at 
        # that point just find the min




        

1,2,3,4,5,6

4,5,6,1,2,3

5,6,1,2,3,4

