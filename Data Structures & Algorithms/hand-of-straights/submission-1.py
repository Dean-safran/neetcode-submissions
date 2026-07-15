class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize) != 0 :
            return False
        
        freq_dict = dict()
        for i in range(len(hand)) :
            if hand[i] not in freq_dict :
                freq_dict[ hand[i] ] = 1
            else :
                freq_dict[ hand[i] ] += 1

        hand.sort() 

        curr_groups = 0 
        num_groups_needed = len(hand) // groupSize
        for i in range(len(hand)) :
            if freq_dict[hand[i]] != 0 :
                for i in range(hand[i], hand[i] + groupSize) :
                    if i not in freq_dict or freq_dict[i] == 0 :
                        return False
                    else :
                        freq_dict[i] -= 1
                curr_groups += 1
            if curr_groups == num_groups_needed :
                return True
            
             





