class Solution:
    def search(self,nums, target):
    # findMinIndex to locate the break in the ascending order
    # in the array (if there is one)
    # is o(log n) with constant space -- the 
    # spliced list at the end is always extremly small 
    # so it's constant. BinarySearch is also o(log n) with 
    # potentially log n space for the call stack. 
    # Overall time is o(log n) and o(1) space. 

    # ToDo : make findMinIndex without slicing and 
    # an iterative binary search

       minIndex = self.findMinIndex(nums)
       if nums[0] == nums[minIndex] : 
           return self.binarySearch(nums, target, 0, len(nums) - 1)
       else : 
           result1 = self.binarySearch(nums, target, 0, minIndex - 1)
           result2 = self.binarySearch(nums, target, minIndex, len(nums) - 1)
           if result1 != -1 : 
               return result1
           elif result2 != -1 :
               return result2
           return -1
        

    def findMinIndex(self, nums) : 
        l = 0
        r = len(nums) - 1

        if len(nums) == 1 : 
            return 0

        while r - l > 1 : 
            mid = l + ( (r - l) // 2 )
            if nums[l] > nums[mid] : 
                r = mid
            else : 
                l = mid
        
        finalPortion = nums[l : r + 1]
        minNumber = min(finalPortion)
        return nums.index(minNumber)
    
    def binarySearch(self, nums, target, l, r) :
        mid = l + ((r - l) // 2)
        
        if r - l <= 3: 
            for i in range(l, r+1) :
                if target == nums[i] :
                    return i
            return -1
        
        if target == nums[mid] : 
            return mid
        if target > nums[mid] : 
            return self.binarySearch(nums, target, mid + 1, r)
        if target < nums[mid] :
            return self.binarySearch(nums, target, l, mid - 1)


        
