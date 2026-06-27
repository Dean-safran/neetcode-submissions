class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time is o(n) : each element and its adjacent (differing by 1)
        # neighbors get processed once each, with constant 
        # addition operations to add to counter, so overall 
        # 
        # space is also o(n) for the set form of the original 
        # list 

        #iter creates a 'bookmark' pointing to first element 
        # in set, next is called on the iterator 
        # , grabs the current element and moves the iterator's pointer 
        # to the next element. For loops implicitly use 
        # an iterator under the hood. This is just a constant 
        # space pointer and a constant o(1) grabbing operation
        # instead of a o(n) time and space creating-a-new-list operation
        
        numSet = set()
        
        numSet.update(nums)  #adds an entire list at once to a set, .add() only adds one element to the set
        result = 0
        while len(numSet) > 0 :
            possibleResult = self.helper(numSet, 1, next(iter(numSet)))
            if possibleResult > result :
                result = possibleResult
        return result
        

    def helper(self, numSet, counter, initialNum) :
        if initialNum not in numSet :
            return counter

        numSet.remove(initialNum)

        if (initialNum + 1) not in numSet and (initialNum - 1) not in numSet :
            return counter

        if (initialNum + 1) in numSet :
            counter = 1 + self.helper(numSet, counter, initialNum + 1)
        if (initialNum - 1) in numSet :
            counter = 1 + self.helper(numSet, counter, initialNum - 1)
        return counter
        
        # my thinking is to start with first element, check 
        # if element + or - 1 is in the set, if yes recursively
        # remove curr and check if their adjacent elements 
        # are in the set, incrementing counter as we go, 
        # if in a current call no neighbors exist and there
        # are still more elements in the array, store the 
        # current counter in a lcs lengths array and set it 
        # equal to 0

        # the problem is how do I implement a recursive algorithm 
        # here, I might have to create a helper function. I'm 
        # also worried about my counters and arrays losing their values 
        # in the recursive algorithm. 

        

        