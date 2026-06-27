import heapq

class MedianFinder:

# sorting : addNum takes o(1) time and space 
#           Findmedian takes o(nlogn) to sort then o(1) to find median

# heap : addNum takes o(logn) time
#        Findmedian takes 

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        """ if time to add to minHeap  :        len(minHeap) <= len(maxheap)
                if num < minHeap_root and num < maxheap_root : 
                    pop maxheap_root and add to min heap, 
                    add num to min heap
                else : 
                    add num to minHeap
            else time to add to maxHeap : 
                if num > maxheap_root and num > minheap_root : 
                    minHeap_root will become maxHeap_root
                    since num > minHeap_root, add num to minHeap
                    maxHeap_root < minHeap_root as required
                else : 
                    add num to maxHeap
        
        """
        if len(self.minHeap) == 0 : 
            self.minHeap += [num]
            return
        if len(self.maxHeap) == 0 : #need to add to maxHeap
            if num > self.minHeap[0] : 
                self.maxHeap += [-(self.minHeap[0])]
                self.minHeap[0] = num
                return
            self.maxHeap += [-num]
            return

        if len(self.minHeap) <= len(self.maxHeap) : 
            if num < self.minHeap[0] and num < -(self.maxHeap[0]) :
                toAdd = -(heapq.heappop(self.maxHeap))
                heapq.heappush(self.minHeap, toAdd)
                heapq.heappush(self.maxHeap, -num)
            else : 
                heapq.heappush(self.minHeap, num)
            return
        else : 
            if num > -(self.maxHeap[0]) and num > self.minHeap[0] : 
                toAdd = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -(toAdd))
                heapq.heappush(self.minHeap, num)
            else : 
                heapq.heappush(self.maxHeap, -(num))
            return


    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap) : 
            return ( -(self.maxHeap[0]) + self.minHeap[0] ) / 2
        if len(self.maxHeap) > len(self.minHeap) : 
            return -(self.maxHeap[0])
        else : 
            return self.minHeap[0]
        