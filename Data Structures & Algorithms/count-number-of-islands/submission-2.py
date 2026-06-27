"""
space is o(m) for recursion call stack 
where m is the amount of blocks on the grid
spanned by the largest island 

time is o(row*col + number of "1" chars on board) = o(row*col)
                                                 ^^^ 
                                        This is because if all the chars
                                        on the board were "1", then we'd
                                        have o(row*col + row*col) = 
                                        o(2*row*col) = o(row*col)


since we do
at least a constant operation (a boolean check for "0" and "#" or a call to 
DFS for "1") on every element in the grid, and DFS visits each "1" once
before turning it into "#"


"""

class Solution:
    def numIslands(self, board: List[List[str]]) -> int:
        
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


        # loop over all rows and cols

        # if the starting block is 0 or #(we already visited), 
        # don't recurse

        # foundNeighbor #

        # DFS on all adjacent neighbors, turning them 
        # into # once visited and before 
        # recursing, if you run into 0 or #, return

