class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         #if diff b/w pointers is 1, you have 
        # to move pointer 2, if pointer2 is at the 
        # end, you have to move pointer 1

        # if we find a number less than pointer1, 
        # set equal to pointer1,put pointer2 next to it
        # if we find a number greater than pointer2, set equal 
        # to pointer2

        # return maxProfit at the end
        
        maxProfit = 0
        pointer1 = 0
        pointer2 = 1
        if len(prices) == 1 : 
            return 0

        for i in range(0, len(prices)) : 

            if prices[i] < prices[pointer1] and (i < len(prices) - 1) :
                pointer1 = i
                pointer2 = i + 1
                continue
            if prices[i] > prices[pointer2] and i > 1 :
                pointer2 = i 

            currProfit = prices[pointer2] - prices[pointer1]
            if currProfit > maxProfit : 
                maxProfit = currProfit
        return maxProfit
            
            


        return maxProfit
            
