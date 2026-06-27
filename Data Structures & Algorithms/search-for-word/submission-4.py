class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        backtrack(params) 
            if base case : 
                result += copy of solution

            for choice in choices : 
                if violates condition(s) : 
                    continue
            
                make choice
                backtrack(updated_params)
                undo_choice

        
        We start paths looping over each row, then an inner loop 
        over each col

        We keep a visited set of row col tuples 

        The current block in [row, col] coords
        and current target_list_index are params

        Calculate rows and cols of board, if you add
        a direction and curr block's row or col is out of range, 
        continue

        if the next block is in visited set, continue
        if the next block is not the same as the next target 
        index, continue

        base case is if i == length of target - 1, 
        if yes return true 
        """

        visited = set()
        rows = len(board)
        cols = len(board[0])
        moves = [(0,1), (1,0), (0,-1), (-1,0)]

        def backtrack(r, c, i) : 
            nonlocal visited, rows, cols, moves
            if ( (min(r, c) < 0) or 
            (r >= rows) or 
            (c >= cols) or
            ((r,c) in visited) or
             board[r][c] != word[i] ) : 
                return False

            if i == len(word) - 1 :
                return True
            visited.add((r,c))
            

            for move in moves : 
                if backtrack(r + move[0], c + move[1], i + 1) :
                    return True
            visited.remove((r,c))
            return False
    
        for row in range(rows) : 
            for col in range(cols) : 
                if backtrack(row, col, 0) :
                    return True
        return False

            
            

        