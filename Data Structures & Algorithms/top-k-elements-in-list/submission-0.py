class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #once we have freq of each # in hashTable, what can we do?
        #sort by value in decreasing order, taking first 
        #k elements in our array
        
        d = {}
        for num in nums :
            if num not in d :
                d[num] = 0
            else : 
                d[num] += 1
        
        new_nums = sorted(d.items(), key = lambda x :x[1], reverse = True)

        result = []
        for index in range(k) :
            result.append(new_nums[index][0])
        return result