class Solution:
    def findMin(self, nums: List[int]) -> int:

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
        # is larger you found min, base case is <=3 elements, at 
        # that point just find the min

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
            
            






        

1,2,3,4,5,6

4,5,6,1,2,3

5,6,1,2,3,4

