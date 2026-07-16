class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # insight -> you can only merge down to preserve info
        
        # so if there are any triplets that have elem[i] > target[i], 
        # we can never use them to make final solution, so we get rid 
        # of them

        # store valid triplets in a list : o(n) space
        filtered_triplets = []
        for i in range(len(triplets)) :
            if (triplets[i][0] > target[0] or
                triplets[i][1] > target[1] or 
                triplets[i][2] > target[2]) :
                continue
            else :
                filtered_triplets += [triplets[i]]
        
        # loop through filtered list 3 times ; o(n) time
        is_num_present = [False, False, False]
        for i in range(3) :
            for j in range(len(filtered_triplets)) :
                if filtered_triplets[j][i] == target[i] : 
                    is_num_present[i] = True

        return is_num_present[0] and is_num_present[1] and is_num_present[2] 
