class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # insight -> you can only merge down to preserve info
        
        # sort by first triplet elem
       
        # find all triplets with target[0]

        # if none have elem[1] <= target[1] or elem[2] <= target[2]
        # return false

        # of the remaining triplets, are there any that have 
        # elem[1] <= target or elem[2] <= target


        # ---------------------
        # search through each triplet
        # if any of the elements are greater than target,
        # get rid of them

        filtered_triplets = []
        for i in range(len(triplets)) :
            if (triplets[i][0] > target[0] or
                triplets[i][1] > target[1] or 
                triplets[i][2] > target[2]) :
                continue
            else :
                filtered_triplets += [triplets[i]]
        
        is_num_present = [False, False, False]
        for i in range(3) :
            for j in range(len(filtered_triplets)) :
                if filtered_triplets[j][i] == target[i] : 
                    is_num_present[i] = True

        return is_num_present[0] and is_num_present[1] and is_num_present[2] 
