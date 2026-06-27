import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #once we have freq of each # in hashTable, what can we do?
        #sort by value in decreasing order, taking first 
        #k elements in our array
        
        #Big(O) : 
        # time : O(nlogn)

        #         O(n) (n being the length of nums) 
        #        + O(nlogn) to sort
        #       each number by freq, where worst case is each number is unique
        #       and you need to sort all n numbers

        # space : O(n) for a dict with at most n keys


        d = {}
        for num in nums :
            if num not in d :
                d[num] = 0
            else : 
                d[num] += 1
        
        d_list = []
        for tup in d.items() :
            new_tup = (-tup[1], tup[0])
            d_list.append(new_tup)
        heapq.heapify(d_list)

        result = []
        for index in range(k) :
            tup = heapq.heappop(d_list)
            result.append(tup[1])
        return result

       
        #slower sorted version

        # new_nums = sorted(d.items(), key = lambda x :x[1], reverse = True)
        # result = []
        # for index in range(k) :
        #     result.append(new_nums[index][0])
        # return result