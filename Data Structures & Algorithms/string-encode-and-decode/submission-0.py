class Solution:
# My first thought was to use _ or a password between separate strings

# My second thought was to turn every char into its unicode number, 
# each separated by c, and each separate string separated by s. this 
# way the delimiter is unambiguous, it's the only letters in a string 
# of numbers

# had to look up length prefixing, fuck


    def encode(self, strs: List[str]) -> str:
        toDecode = ""
        for i in strs : 
            length = len(i)
            toDecode += (str(length) + "#")
            toDecode += i
        return toDecode

    def decode(self, s: str) -> List[str]:
        result = []
        while len(s) > 0 :
            hashIndex = s.find("#")
            num = int(s[0:hashIndex])
            s = s[hashIndex + 1 :]
            word = s[0 : num]
            result.append(word)
            s = s[num :]
        return result
