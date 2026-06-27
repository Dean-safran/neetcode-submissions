class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #find the two highest ints that are the farthest apart
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