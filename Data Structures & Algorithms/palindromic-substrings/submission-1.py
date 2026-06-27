"""
add special character sentinels to end to indicate end of string

treat every char as center, if you can expand left and right pointer
increase result by 1, otherwise move on 
"""

"""
o(n) time to run manacher's with o(n) space, loop at the 
end is also an o(n) operation with constant additions to result
"""

"""
how-to-use Manacher's idea : the radius of a center in transformed
string //2 is how many palins you can make with center in original 
string, if the center is odd, then you need to add one to include 
the center itself as a palindrome

at the end we do a loop through the radius array 

if the center is a special char and its radius is not 0, then 
you //2

if it's not a special char, then //2 and add one 
(since you can make a palin with the center itself)

if the palin is of length 1 and isn't a special char,
don't divide by 2, just add 1 to result 
(you'd get 0 if you divided by two, which isn't right you 
CAN make 1 palindrome with that char) 
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        #pre-process string

        t = "^"
        for ch in s :
            t += "$" + ch
        t += "$#"

        L, R = 0, -1
        p = [0] * len(t)

        for i in range(1, len(t) - 1) :
            if i < R :
                center = (L + R) // 2
                mirror_index = center - (i - center)
                p[i] = min(R - i, p[mirror_index])
            
            #expansion loop
            l_pointer = i - p[i]
            r_pointer = i + p[i]
            while t[l_pointer - 1] == t[r_pointer + 1] :
                l_pointer -= 1
                r_pointer += 1
                p[i] += 1
            if r_pointer > R :
                L = l_pointer
                R = r_pointer

        result = 0
        for i in range(1, len(p) - 1) : 
            if t[i] != "$" and p[i] == 1 :
                result += p[i]
            elif t[i] == "$" and p[i] != 0 :
                result += p[i] // 2
            elif t[i] != "$":
                result += (p[i] // 2) + 1
        return result
            
        







