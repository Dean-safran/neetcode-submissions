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

        how to optimize time?

        """

        seen = set()
        for i in range(len(nums)) :
            if nums[i] not in seen :
                seen.add(nums[i])
            else :
                return nums[i]