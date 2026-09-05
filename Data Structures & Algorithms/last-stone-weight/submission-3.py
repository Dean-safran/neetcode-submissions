import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)) : 
            stones[i] = -stones[i]
        heapq.heapify(stones)
        curr = 0
        while len(stones) > 1 : 
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 == stone2 :
                curr = 0
            else : 
                curr = stone1 - stone2
                heapq.heappush(stones, curr)
        if len(stones) == 1 : 
            curr = stones[0]
        return -curr