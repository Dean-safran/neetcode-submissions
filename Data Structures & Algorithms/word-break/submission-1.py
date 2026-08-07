class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        try all possibilities starting at first possible word, 
        then recursing on rest of string

        recurrence relation : 
            let f(i) be True if the suffix of str s
            starting at index i can be split into 
            dictionary words

            f(n), where n = len(s), is True since 
            an empty string is split

            f(i) = s[i:j] is an element of wordDict AND f(j) where j = i+1
        """
        memo = {}
        def helper(curr_string) : 
            if curr_string in memo :
                return memo[curr_string]
                
            if len(curr_string) == 0 : 
                return True

            curr_word = ""
            for i in range(len(curr_string)) :
                curr_word += curr_string[i]
                found_solution = False

                if curr_word in wordDict : 
                    next_start_idx = i + 1
                    if next_start_idx == len(curr_string) :
                        return True
                    else : 
                        found_solution = helper(curr_string[next_start_idx:])
                        memo[curr_string[next_start_idx:]] = found_solution
                        if found_solution :
                            break
                
                if not found_solution :
                    continue
            return found_solution
            
        return helper(s)
            