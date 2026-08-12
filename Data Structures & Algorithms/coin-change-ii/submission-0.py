class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """ 

        state/choice at each coin -> include or don't include the current in in the set of coins

        what is the recurrence relation, how can we make sure path 1,1,2 and 2,1,1 is only
        counted as one path 
        """
        paths = dict()
        def helper(amount, index) :
            if (amount, index) in paths:
                return paths[(amount, index)]
            if amount == 0 :
                paths[(amount, index)] = 1
                return 1
            elif amount < 0 or index > len(coins) - 1: 
                paths[(amount, index)] = 0
                return 0
            res = 0
            res += helper(amount - coins[index], index)
            res += helper(amount, index + 1)
            paths[(amount, index)] = res
            return res
        
        return helper(amount, 0)