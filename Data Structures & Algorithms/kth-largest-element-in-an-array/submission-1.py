import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        o(n) time for heapify
        o(klogn) time for finding largest element
        o(n) space for heap

        """

        for i in range(len(nums)) : 
            nums[i] = -nums[i]
        heapq.heapify(nums)
        for _ in range(k) :
            curr = heapq.heappop(nums)
        return -curr