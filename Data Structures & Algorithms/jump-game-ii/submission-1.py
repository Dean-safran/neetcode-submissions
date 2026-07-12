class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        end = len(nums) - 1
        num_jumps = 0

        next_r = -1
        while r < end : 
            num_jumps += 1
            for i in range(l,r + 1) : 
                if i + nums[i] > next_r : 
                    next_r = i + nums[i]
            l = r + 1
            r = next_r
        return num_jumps

        # # scan backwards from end elem
        # # find smallest idx elem that can reach curr end
        # # set end to that elem

        # end = len(nums) - 1
        # num_jumps = 0
        # while end != 0 :
        #     next_end = -1
        #     # find minimum idx that can reach curr end
        #     for i in range(end - 1, -1, -1) :
        #         if i + nums[i] >= end : 
        #             next_end = i 
        #     end = next_end
        #     num_jumps += 1
        # return num_jumps