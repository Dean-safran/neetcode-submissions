"""DP algorithm : time o(n^2), space o(1) 

 keep a global largest_diff = (start, finish)  #indexes

 If start < 0 or finish > len(s) - 1, continue to next center
 
 do an odd pass, treating each letter as the center of an odd length
 palindrome and extending out. Start, Finish start in the same place, 
 then -=1 and += 1, respectfully. If diff is greater than global 
 diff, update largest_diff.

 do an even pass, treating each letter and it's right neighbor 
 as the center of an even length palindrome and extending out.
 Start, Finish start one ch apart , 
 then -=1 and += 1, respectfully. If diff is greater than global 
 diff, update largest_diff.

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #preprocessing
        t = "^"
        for ch in s :
            t += "$" + ch
        t += "$#"

        L, R = 0, -1
        p = [0] * len(t)

        for i in range(1, len(t) - 1) :
            if i <= R :
                center = (R + L) // 2
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

        max_radius = max(p)
        max_center_index = p.index(max_radius)
        start = max_center_index - max_radius

        #converting lengths to original string 
        real_start = start // 2
        real_len = ( 1 + (2 * max_radius) ) // 2
        return s[real_start : real_start + real_len]

            

            

