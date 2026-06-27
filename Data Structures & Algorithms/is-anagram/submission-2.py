class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #create dict of char's and freq of each char 
        #for each str    o(n + m)

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

        for key in dict1 : 
            if key not in dict2:
                return False
            if dict1[key] != dict2[key] :
                return False
        for key in dict2 : 
            if key not in dict1:
                return False
            if dict1[key] != dict2[key] :
                return False
        return True


        