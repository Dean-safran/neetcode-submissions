class Solution:
    def isPalindrome(self, s: str) -> bool:  
        pointer1 = 0
        pointer2 = len(s) - 1

        while True : 
            if (pointer2 - pointer1) < 0 :
                return True
            
            if not self.isAlphaNum(s[pointer1]) :
                pointer1 += 1
                continue
            if not self.isAlphaNum(s[pointer2]) :
                pointer2 -= 1
                continue
            
            ch1 = s[pointer1].lower()
            ch2 = s[pointer2].lower()
            if ch1 != ch2 :
                return False 
            pointer1 += 1
            pointer2 -= 1

                


    def isAlphaNum(self, ch) :
        if ("a" <= ch.lower() <= "z") or ("0" <= ch <= "9") :
            return True 
        return False 
         