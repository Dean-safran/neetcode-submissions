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

        #This checks if each dict has the same key value pairs

        return dict1 == dict2

        