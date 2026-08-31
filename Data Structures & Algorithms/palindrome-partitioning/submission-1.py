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

            # you must start new with first ch
            if i == 0 :
                curr_strings[-1] = s[i]
                DFS(i+1)
            else : 
                # try extending curr str
                curr_strings[-1] += s[i]
                DFS(i+1)
                curr_strings[-1] = curr_strings[-1][:-1]
                # try starting new str
                curr = curr_strings[-1]
                # don't start new if curr is not a palindrome (prune)
                if not is_palindrome(0, len(curr) - 1, curr) :
                    return
                curr_strings.append(s[i])
                DFS(i+1)
                del curr_strings[-1]
            return
        
        res = []
        curr_strings = ["",]
        DFS(0)
        return res


