class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1) : 
            temp = str2
            str2 = str1
            str1 = temp

        for i in range(len(str2), 0, -1) :
            candidate = str2[:i]

            if len(str1) % i == 0 and len(str2) % i == 0 :
                if ((candidate * (len(str1) // i) == str1) and 
                   (candidate * (len(str2) // i) == str2)) :
                   return candidate
        return ""