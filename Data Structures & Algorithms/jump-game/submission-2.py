class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        curr_idx = 0

        while curr_idx < end :

            # If can jump to end, return true
            if end - curr_idx <= nums[curr_idx] :
                return True

            # Of possible jumps, jump to
            # the one with max val
            next_idx = -1
            max_jump = 0
            for possible_jump in range(1, nums[curr_idx] + 1) :
                curr_jump = curr_idx + possible_jump + nums[curr_idx + possible_jump]
                if curr_jump > max_jump :
                    max_jump = curr_jump
                    next_idx = curr_idx + possible_jump
                    
            # Couldn't get to end, next vals 
            # are all zero
            if next_idx == -1 :
                return False
            # Found next elem, go to it
            else :
                curr_idx = next_idx
        return True
