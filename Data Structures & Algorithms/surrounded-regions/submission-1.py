class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """

        union find comes to mind first, but we can 
        also recursively search each 0, if it or any 
        0 reachable is an edge piece, add to 0 visited, otherwise
        mark helper true and set all X visited to X


        """

        keep = set()

        def keep_0s(row, col, board) : 
            dirs = [(0,1), (0,-1), (1,0), (-1,0),]
            keep.add((row,col))
            for move in dirs : 
                dy, dx = move
                new_row = row + dy
                new_col = col + dx

                if (new_row < 0 or 
                    new_row > len(board) - 1 or
                    new_col < 0 or 
                    new_col > len(board[0]) - 1
                    ) :
                    continue
                if board[new_row][new_col] == "X" :
                    continue
                if (new_row, new_col) in keep : 
                    continue
                if board[new_row][new_col] == "O" : 
                    keep_0s(new_row, new_col, board)

        for i in range(len(board)) :
            if (i, 0) in keep : 
                continue
            if board[i][0] == "O" :
                keep_0s(i, 0, board)
        for i in range(1, len(board[0])) : 
            if (0, i) in keep : 
                continue
            if board[0][i] == "O" :
                keep_0s(0, i, board)
        for i in range(1, len(board[0])) : 
            if (len(board)-1, i) in keep : 
                continue
            if board[len(board)-1][i] == "O" :
                keep_0s(len(board)-1, i, board)
        for i in range(1, len(board)-1) :
            if (i, len(board[0])-1) in keep : 
                continue
            if board[i][len(board[0])-1] == "O" :
                keep_0s(i, len(board[0]) - 1, board)
        
        for i in range(len(board)) :
            for j in range(len(board[0])) : 
                if board[i][j] == "O" and (i,j) not in keep :
                    board[i][j] = "X"
        
                