class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #find the two highest ints that are the farthest apart
        # if one pointer's height is smaller than the other, 
        #move it in because it's holding the currVol back!

        # time o(n), space o(1) since pointers are constant 
        # space, they're integer values. We move each pointer
        # one at a time, each element in array is processed 
        # once, we do constant comparisons after each pointer 
        # is moved, so total time is o(n), n being the length 
        # of the heights list

        pointer1 = 0
        pointer2 = len(heights) - 1
        maxVol = -1
        while pointer1 < pointer2 : 
            height1 = heights[pointer1]
            height2 = heights[pointer2]
            
            currVol = (pointer2 - pointer1) * min(height1, height2)
            
            if currVol > maxVol : 
                maxVol = currVol

            if height1 < height2 : 
                pointer1 += 1
            else : 
                pointer2 -= 1

        return maxVol