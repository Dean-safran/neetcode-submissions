class Solution:
# My first thought was to use _ or a password between separate strings

# My second thought was to turn every char into its unicode number, 
# each separated by c, and each separate string separated by s. this 
# way the delimiter is unambiguous, it's the only letters in a string 
# of numbers

# had to look up length prefixing, fuck

#Big O : 
#  Time --> encode is O(n) where n is number of chars
# 
#  decode is O(n) for scanning through every char of s 
#  and we splice out each string and its
#  corresponding length char once
#  so that totals to roughly the length of the string, o(n)
#  total time is o(2n) which is o(n)


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
            # *pointer* points to the start 
            # of a new word's length prefix,
            # in order to ensure the hashtag 
            # we're checking is part of a prefix,
            # and not the next string,
            # it must come right after the pointer (the
            # number part of the prefix), hence the second bool i > pointer
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
