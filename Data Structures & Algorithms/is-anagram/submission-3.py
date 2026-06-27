class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # create dict of char's and freq of each char 
        # for each str    o(n + m)
        # this is o(1) space because no matter the string size, 
        # each dict is max 26 keys, which 
        # is constant space in terms of input

        dict1 = {}
        dict2 = {}
        for ch in s : 
            if ch not in dict1 : 
                dict1[ch] = 1
            else : 
                dict1[ch] += 1
        for ch in t : 
            if ch not in dict2 : 
                dict2[ch] = 1
            else : 
                dict2[ch] += 1

        #for each key in str s, check if it's in t's dict  
        #o(n) w/ o(1) checks
        # if yes, check if the value (freq) is the same

        return dict1 == dict2

        