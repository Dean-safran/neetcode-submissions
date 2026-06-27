class Solution:
    def numIslands(self, board: List[List[str]]) -> int:
        # loop over all rows and cols

        # if the starting block is 0 or #(we already visited), 
        # don't recurse

        # foundNeighbor #

        # DFS on all adjacent neighbors, turning them 
        # into # once visited and before 
        # recursing, if you run into 0 or #, return
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def DFS(r,c) :
            if (min(r,c) < 0 or r >= len(board) or
                c >= len(board[0]) or
                board[r][c] == "0" or board[r][c] == "#") :
                return
            board[r][c] = "#"
            for dy,dx in moves :
                DFS(r + dy, c + dx)
        
        result = 0
        for row in range(len(board)) :
            for col in range(len(board[0])) :
                if board[row][col] == "0" or board[row][col] == "#" :
                    continue
                DFS(row, col)
                result += 1

        return result

