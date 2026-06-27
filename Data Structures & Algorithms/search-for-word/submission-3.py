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
            if (r,c) == (-1,-1) : 
                for row in range(rows) : 
                    for col in range(cols) : 
                        if backtrack(row, col, 0) :
                            return True
                return False
            
            # if you're continuing a path, not starting one,
            # do the following : 

            # add current block to visited

            # for move in moves : 
            # if next move is in bounds and it matches next 
            # index of target string, recurse
            # else : remove block from visited and continue
            if board[r][c] != word[i] : 
                return False
            if i == len(word) - 1 :
                return True
            visited.add((r,c))
            

            for move in moves : 
                next_row = r + move[0]
                next_col = c + move[1]
                if 0 <= next_row and next_row < rows and 0 <= next_col and next_col < cols : 
                    if (next_row, next_col) not in visited : 
                        if backtrack(next_row, next_col, i + 1) :
                            return True
            visited.remove((r,c))
            return False
    
        return backtrack(-1, -1, 0)

            
            

        