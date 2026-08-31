class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """

        make an is_palindrome(s: str) function

        we either start new or add to curr substring

        """

        def is_palindrome(l, r, s) :
            while l < r :
                if s[l] == s[r] :
                    l += 1
                    r-= 1
                else : 
                    return False
            return True
        
        def DFS(i) :
            if i > len(s) - 1 : 
                for string in curr_strings :
                    if not is_palindrome(0, len(string)-1, string) :
                        return 
                res.append(curr_strings.copy())
                return

            # try extending curr str
            curr_strings[-1] += s[i]
            DFS(i+1)
            curr_strings[-1] = curr_strings[-1][:-1]
            
            # don't start new if curr is not a palindrome (prune)
            curr = curr_strings[-1]
            if is_palindrome(0, len(curr) - 1, curr) :
                # try starting new str
                curr_strings.append(s[i])
                DFS(i+1)
                curr_strings.pop()
            return
        
        res = []
        if not s :
            return [[]]

        curr_strings = [s[0],]
        DFS(1)
        return res


