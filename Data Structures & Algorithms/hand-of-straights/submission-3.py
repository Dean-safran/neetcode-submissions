class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0 :
            return False
        
        hand.sort()
        freq = dict()
        for num in hand : 
            if num not in freq : 
                freq[num] = 1
            else :
                freq[num] += 1
        
        for i in range(len(hand) - groupSize + 1) : 
            if freq[hand[i]] == 0 :
                continue
            for j in range(hand[i], hand[i] + groupSize) : 
                if j not in freq or freq[j] == 0 :
                    return False
                freq[j] -= 1
        return True





