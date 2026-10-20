class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r :
            if numbers[l] + numbers[r] > target :
                r -= 1
            elif numbers[l] + numbers[r] < target :
                l += 1
            elif numbers[l] + numbers[r] == target :
                return [l+1, r+1]

        
        
        
        
        
        
        
        
        
        # for i in range(len(numbers) - 1) : 
        #     for j in range(i+1, len(numbers)) :
        #         if numbers[i] + numbers[j] == target :
        #             return [i+1, j+1]
        # return [0,0]