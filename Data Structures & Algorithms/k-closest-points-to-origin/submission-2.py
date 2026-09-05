class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        keep a max heap of tuples (distance, (x, y))
        push a point
        if len(points) > k, pop farthest point

        time -> nlogk, pushing each point onto the heap of size k
        space -> o(k) for the heap 

        """

        heap = []
        for x,y in points :
            distance = -( (x ** 2) + (y ** 2) )
            heapq.heappush(heap, (distance, (x,y)))
            if len(heap) > k :
                heapq.heappop(heap)
        res = []
        for point in heap : 
            res.append(point[1])
        return res