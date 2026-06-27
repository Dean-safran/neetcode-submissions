class Solution:
# My first thought was to use _ or a password between separate strings

# My second thought was to turn every char into its unicode number, 
# each separated by c, and each separate string separated by s. this 
# way the delimiter is unambiguous, it's the only letters in a string 
# of numbers

# had to look up length prefixing, fuck

#Big O : 
#  Time --> encode is O(n * k) where n is number of strings
#  and k is the length of the longest string
#  decode is O(n) for the appending of each word


    def encode(self, strs: List[str]) -> str:
        toDecode = ""
        for i in strs : 
            length = len(i)
            toDecode += (str(length) + "#")
            toDecode += i
        return toDecode

   
    def decode(self, s: str) -> List[str]:
        result = []
        pointer = 0
        for i in range(len(s)) :
            if s[i] == "#" and i > pointer :
                num = s[pointer : i]
                num = int(num)
                pointer = i + 1 + num
                word = s[i+1 : i + 1 + num]
                result.append(word)
        return result
 

        # while len(s) > 0 :
        #     hashIndex = s.find("#")
        #     num = int(s[0:hashIndex])
        #     pointer = hashIndex + 1
        #     word = s[pointer : num]
        #     result.append(word)
        #     pointer += num
        # return result
