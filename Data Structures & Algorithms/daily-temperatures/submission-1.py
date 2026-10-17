import heapq
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """

        for each day, scan the rest of list to find 
        number greater than curr (n^2 time)

        walk through temps, if a greater number 
        is found, update backwards if value is 0
        keep track of values that need numbers assigned

        """
        res = [0 for _ in range(len(temperatures))]
        stack = [0]
        for i in range(1, len(temperatures)) :
            if stack : 
                while temperatures[i] > temperatures[stack[-1]] :
                    idx = stack[-1]
                    del stack[-1]
                    res[idx] = i - idx
                    if not stack :
                        break
                stack.append(i)
            else : 
                stack.append(i)
        return res
        
        
        
        
        # results = [0 for _ in range(len(temperatures))]
        # for i in range(len(temperatures)) :
        #     for j in range(i+1, len(temperatures)) : 
        #         if temperatures[j] > temperatures[i] :
        #             results[i] = j - i
        #             break
        # return results

