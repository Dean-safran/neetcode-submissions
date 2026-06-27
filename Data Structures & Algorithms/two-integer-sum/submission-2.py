class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #making dict with each number and its index
        d = {}
        dCounter = 0
        for num in nums : 
            d[num] = dCounter
            dCounter += 1
        
        numIndex = 0
        for num in nums : 
            num2 = target - num
            if num2 in d :
                if numIndex < d[num2] :
                    return [numIndex, d[num2]]
                if numIndex > d[num2] :
                    return [d[num2], numIndex]
            numIndex += 1


