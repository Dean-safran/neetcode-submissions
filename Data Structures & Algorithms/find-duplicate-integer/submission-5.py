class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """

        brute force -> compare each number with every other number 
        time -> o(n^2)
        space -> o(1)

        or make a seen set, loop through array, if element in seen 
        return element
        time -> o(n)
        space -> o(n)

        """

        slow = 0
        fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast :
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow1 = 0
        while nums[slow1] != nums[slow] :
            slow1 = nums[slow1]
            slow = nums[slow]
        return nums[slow]
        