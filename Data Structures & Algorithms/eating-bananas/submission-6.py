class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        brute force 
        -----------
        loop through possible eating speeds,
        which includes 1 through the max pile amount
        (using max pile amount or more results in each
        pile taking 1 hour, so use max pile amount since it's smallest)

        add total time to variable, if at any point
        we exceed max time, try next largest eating speed



        The optimization is binary searching the eating speeds?

        Start at middle eating speed
            if we are at time, return curr eating speed

            if we are over time, 
            search larger eating speeds

            if we are under time,
            search lower eating speeds

            

        """

        max_eating_speed = max(piles)

        def time_to_eat(eating_speed) :
            total = 0
            for j in range(len(piles)) :
                total += (piles[j] + eating_speed - 1) // eating_speed
            return total

        l = 1
        r = max_eating_speed
        while l <= r :
            m = (l+r) // 2
            time = time_to_eat(m)
            
            if time > h :
                l = m + 1
                continue
            
            if time <= h :
                r = m - 1
                continue
        return l
        