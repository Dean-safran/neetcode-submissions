class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # brute force -> for each num in list, 
        # loop through list to find match
        # except for num itself

        # or can do one pass over the list
        # and make a dictionary, then loop
        # through the dictionary
        ans = 0
        for i in range(len(nums)) :
            ans ^= nums[i]
        return ans
