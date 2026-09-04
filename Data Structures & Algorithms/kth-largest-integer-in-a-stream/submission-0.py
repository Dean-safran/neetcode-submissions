import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        for i in range(len(self.nums)) : 
            self.nums[i] = -self.nums[i]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        temp = []
        curr = None
        for i in range(len(self.nums) - (len(self.nums) - self.k)) :
            curr = heapq.heappop(self.nums)
            temp.append(curr)
        for i in range(len(temp)) :
            heapq.heappush(self.nums, temp[i])
        return -curr
        